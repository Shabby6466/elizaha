import re
import random
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Enhanced Reflection dictionary
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you": "me",
    "your": "my",
    "yours": "mine",
    "me": "you",
    "myself": "yourself",
    "i'm": "you are",
    "you're": "I am",
    "am": "are"
}

def reflect(fragment):
    words = fragment.lower().split()
    for i in range(len(words)):
        if words[i] in reflections:
            words[i] = reflections[words[i]]
    return " ".join(words)

# MAHAHA Knowledge Base - 50 Solution-Oriented & Rogerian Patterns
patterns = [
    # 1. Solution-Focused (Miracle Question)
    (r"(.*) miracle (.*)|(.*) if (.*) better (.*)", [
        "If a miracle happened tonight and your issue with {0} was gone, what's the first thing you'd notice tomorrow?",
        "Suppose things were suddenly better. What would you be doing differently?",
        "What small sign would tell you that the miracle is starting to happen?"
    ]),
    # 2. Need / Want
    (r"I need (.*)", [
        "What is it about {0} that feels essential to your progress right now?",
        "If you had {0}, how would that change the way you see yourself?",
        "Is {0} something you've needed for a long time, or is it a new feeling?"
    ]),
    # 3. Emotions (Generalized)
    (r"I am feeling (.*)|I feel (.*)", [
        "I hear that you're feeling {0}. What's the most challenging part of that feeling?",
        "If your {0} were trying to protect you from something, what would it be?",
        "How does that feeling of {0} manifest in your day-to-day life?"
    ]),
    # 4. State of Being
    (r"I am (.*)|I'm (.*)", [
        "What does being {0} look like to those around you?",
        "Is there a part of you that isn't {0}?",
        "How long have you carried this identity of being {0}?"
    ]),
    # 5. Interpersonal (You/Me)
    (r"I (.*) you", [
        "In our space here, what is it about the way I am that makes you {0} me?",
        "How does feeling {0} toward me mirror other relationships in your life?",
        "What would you like to say to me about why you {0} me?"
    ]),
    # 6. Self-Reflection
    (r"I (.*) myself", [
        "When you {0} yourself, what's the voice in your head actually saying?",
        "Does {0}ing yourself help you solve your problems, or does it hold you back?",
        "What would it feel like to offer yourself a bit of kindness instead of {0}ing yourself?"
    ]),
    # 7. Family: Mother
    (r"(.*) mother(.*)", [
        "Mothers often leave a deep imprint. How does yours influence your current issue?",
        "What's one thing your mother taught you that you're trying to unlearn?",
        "If you could talk to your mother as an equal right now, what would you say?"
    ]),
    # 8. Family: Father
    (r"(.*) father(.*)", [
        "How has your father's presence (or absence) shaped your understanding of strength?",
        "In what ways do you see your father's patterns repeating in your own life?",
        "What do you need from your father that you might have to give to yourself now?"
    ]),
    # 9. Family: General
    (r"(.*) family(.*)", [
        "Family dynamics can be a heavy load. Where do you fit in that system?",
        "Who in your family understands you the least? Why is that?",
        "What's a family tradition or belief that you're ready to let go of?"
    ]),
    # 10. Childhood
    (r"(.*) child(.*)|(.*) kid(.*)|(.*) young(.*)", [
        "What did that younger version of you need that they didn't get?",
        "How much of what you're feeling now is connected to being a {1}?",
        "If you could hug your younger self, what would you whisper to them?"
    ]),
    # 11. Generalizations: Always
    (r"(.*) always (.*)", [
        "When we say 'always', we sometimes hide the exceptions. When was a time it *didn't* happen?",
        "Does the idea that it's 'always' this way make you feel safe or trapped?",
        "What would happen if just once, it *wasn't* {1}?"
    ]),
    # 12. Generalizations: Never
    (r"(.*) never (.*)", [
        "Is 'never' a fact, or is it a feeling of exhaustion?",
        "What would be different if you believed that 'never' could become 'sometimes'?",
        "Tell me about a time you came very close to it *not* being never."
    ]),
    # 13. Explanations (Because)
    (r"(.*) because (.*)", [
        "Is {1} the whole story, or just the part that's easiest to see?",
        "How does that reason help you change the situation?",
        "Suppose {1} wasn't the cause. What other possibility could there be?"
    ]),
    # 14. Questions to Bot
    (r"Why don't you (.*)|You should (.*)", [
        "It sounds like you're looking for a specific kind of guidance. What would that change for you?",
        "If I were to {0}, what would you learn about yourself?",
        "Are you asking because you're unsure of your own next step?"
    ]),
    # 15. Capability
    (r"I can't (.*)", [
        "What would happen if you *did* {0}?",
        "What's the very smallest part of {0} that you *could* do today?",
        "Who convinced you that you can't {0}?"
    ]),
    # 16. Preferences
    (r"I like (.*)", [
        "What is it about {0} that makes life feel a bit more manageable?",
        "Does {0} represent a value that is important to you?",
        "Tell me more about the comfort you find in {0}."
    ]),
    # 17. Collective (Everyone)
    (r"Everyone (.*)|Everybody (.*)", [
        "When you think of 'everyone', who is the one person that stands out?",
        "Does the idea of 'everyone' {0} make you feel isolated or just tired?",
        "Is there anyone you know who *doesn't* {0}?"
    ]),
    # 18. Dreams
    (r"(.*) dream(.*)", [
        "Dreams often show us what we're ignoring. What was the most vivid part?",
        "If you were the director of that dream, what would the title be?",
        "How did you feel the moment you woke up from the dream?"
    ]),
    # 19. Friends
    (r"(.*) friend(.*)", [
        "How do your friends react when you're going through this?",
        "What do you wish your friends understood about your situation?",
        "Is there a friend you've been avoiding lately?"
    ]),
    # 20. Technology / AI
    (r"(.*) computer(.*)|(.*) machine(.*)|(.*) AI(.*)|(.*) bot(.*)", [
        "Does it feel safer to share these things with a machine like me?",
        "In what ways am I limited in helping you? In what ways am I not?",
        "What do you think is the biggest difference between my logic and your soul?"
    ]),
    # 21. Greetings
    (r"Hello(.*)|Hi(.*)|Hey(.*)", [
        "Hello. I'm MAHAHA. I'm here to explore your world with you. What's unfolding today?",
        "Hi there. I'm glad you've come. What's the heaviest thing on your mind?",
        "Welcome. Let's make this space useful for you. What shall we talk about?"
    ]),
    # 22. Resistance
    (r"No", [
        "Your 'no' is clear. What are you setting a boundary against?",
        "Tell me more about what that 'no' protects for you.",
        "What would it take to turn that 'no' into a 'not right now'?"
    ]),
    # 23. Agreement
    (r"Yes", [
        "That 'yes' sounds like a beginning. What are you ready for?",
        "What does it mean for your future to say 'yes' to this?",
        "How does that 'yes' feel in your chest?"
    ]),
    # 24. Performance / Work
    (r"(.*) job(.*)|(.*) work(.*)|(.*) career(.*)", [
        "How much of your worth is tied to what you produce at {1}?",
        "If you didn't have to work, who would you be?",
        "What's one thing you'd change about your workspace to feel more at peace?"
    ]),
    # 25. Money / Financials
    (r"(.*) money(.*)|(.*) cash(.*)|(.*) bills(.*)", [
        "Money is often about safety. What are you afraid of losing?",
        "How does your current financial situation affect your self-esteem?",
        "If you had all the money you needed, what problem would still be there?"
    ]),
    # 26. Sadness
    (r"(.*) sad(.*)|(.*) unhappy(.*)|(.*) depressed(.*)", [
        "It sounds like you're in a dark valley. How can I walk with you there?",
        "When the sadness of {0} is at its peak, what do you usually do?",
        "If your sadness were a weather pattern, what would it look like?"
    ]),
    # 27. Anger
    (r"(.*) angry(.*)|(.*) mad(.*)|(.*) hate (.*)", [
        "Anger is often a shield for pain. What is your anger trying to protect?",
        "Where do you feel that heat in your body when you're {1}?",
        "What would happen if you let that anger out in a safe way?"
    ]),
    # 28. Anxiety / Fear
    (r"(.*) anxious(.*)|(.*) afraid(.*)|(.*) worry (.*)", [
        "Anxiety is the mind trying to solve the future. What are you trying to solve?",
        "If the thing you're {1} of actually happened, would you be able to handle it?",
        "What's one thing that makes you feel safe when you're {1}?"
    ]),
    # 29. Success / Goals
    (r"(.*) succeed(.*)|(.*) goal(.*)|(.*) achieve(.*)", [
        "What does 'success' actually look like for your soul, not your ego?",
        "What's the very first step toward {1} that you can take tonight?",
        "If you achieved {1}, who would be the first person you'd tell?"
    ]),
    # 30. Failure
    (r"(.*) fail(.*)|(.*) failure(.*)", [
        "Failure is just data. What is this 'failure' telling you about your path?",
        "Is the fear of {1} keeping you from trying something important?",
        "What would you do if you knew you couldn't fail?"
    ]),
    # 31. Relationships (Romantic)
    (r"(.*) love (.*)|(.*) partner(.*)|(.*) dating(.*)", [
        "Relationships are mirrors. What are you seeing reflected in {1}?",
        "What do you need from a partner that you haven't been able to ask for?",
        "How has your experience with {1} changed the way you see yourself?"
    ]),
    # 32. Loneliness
    (r"(.*) lonely(.*)|(.*) alone(.*)", [
        "There's a difference between being alone and being lonely. Which one are you?",
        "What is the loneliness of {0} trying to tell you about your needs?",
        "When do you feel most connected to the world, even when you're by yourself?"
    ]),
    # 33. Health / Body
    (r"(.*) health(.*)|(.*) body(.*)|(.*) sick(.*)", [
        "How is your body responding to the stress you've been carrying?",
        "What's one thing you can do to be kinder to your body today?",
        "If your body could write you a letter, what would it say?"
    ]),
    # 34. Future
    (r"(.*) future (.*)|(.*) tomorrow (.*)", [
        "The future is unwritten. What's one thing you want to make sure you include?",
        "Does the idea of {1} bring you hope or a sense of dread?",
        "What can you do *today* that your future self will thank you for?"
    ]),
    # 35. Past
    (r"(.*) past (.*)|(.*) yesterday (.*)", [
        "The past is a heavy suitcase. What are you ready to unpack and leave behind?",
        "How much of {1} is still dictating your choices today?",
        "If you could go back and change one thing, would you really want to?"
    ]),
    # 36. School / Education
    (r"(.*) school(.*)|(.*) college(.*)|(.*) university(.*)", [
        "Does your academic life feel representative of who you really are?",
        "What's the most valuable lesson you've learned that wasn't in a textbook?",
        "How does the pressure of {1} affect your mental health?"
    ]),
    # 37. Time
    (r"(.*) time (.*)", [
        "Time is our most precious resource. How much of yours is escaping you?",
        "Do you feel like you're running out of time, or waiting for it to begin?",
        "If you had one extra hour every day, what would you do with it?"
    ]),
    # 38. Death / Loss
    (r"(.*) die (.*)|(.*) death (.*)|(.*) lost (.*)", [
        "Grief is a long road. Where are you on that journey right now?",
        "What is one memory of {1} that still brings you a smile?",
        "How has loss changed the way you value your own life?"
    ]),
    # 39. Hobbies
    (r"(.*) hobby(.*)|(.*) play(.*)|(.*) game(.*)", [
        "When you're doing {1}, do you feel like your true self?",
        "How does {1} help you process the harder parts of your day?",
        "What's one thing you love about {1} that most people don't understand?"
    ]),
    # 40. Pets / Animals
    (r"(.*) dog(.*)|(.*) cat(.*)|(.*) pet(.*)", [
        "Animals have a way of seeing us without judgment. What does your pet see when they look at you?",
        "What have you learned about unconditional love from your {1}?",
        "How does having a {1} change the energy of your home?"
    ]),
    # 41. Travel / Escapism
    (r"(.*) travel(.*)|(.*) trip(.*)|(.*) escape (.*)", [
        "Are you traveling toward something, or away from something?",
        "If you could go anywhere in the world right now, where would your soul find rest?",
        "What do you hope to find in {1} that you can't find here?"
    ]),
    # 42. Sleep / Exhaustion
    (r"(.*) sleep(.*)|(.*) tired(.*)|(.*) exhausted(.*)", [
        "Exhaustion is the body's way of saying 'enough'. What are you ready to stop fighting?",
        "What keeps you awake at night when your body is begging for rest?",
        "How would a full night of deep sleep change your perspective on your problem?"
    ]),
    # 43. Change
    (r"(.*) change (.*)", [
        "Change is uncomfortable, but so is staying the same. Which discomfort is more useful?",
        "What's the one thing you're most afraid of losing if you change?",
        "If you changed {1} tomorrow, what would be the best possible outcome?"
    ]),
    # 44. Hope
    (r"(.*) hope (.*)", [
        "Hope is a small light. Where do you see it flickering right now?",
        "What's one thing that still makes you believe things can get better?",
        "If hope were a person, what would they be saying to you?"
    ]),
    # 45. Decisions
    (r"(.*) decide (.*)|(.*) choice (.*)", [
        "What's making this decision so difficult for you?",
        "If you flipped a coin, which side would you secretly hope it lands on?",
        "What's the worst that could happen if you chose the 'wrong' path?"
    ]),
    # 46. Responsibility
    (r"(.*) responsible (.*)|(.*) fault (.*)", [
        "Are you carrying a weight that doesn't belong to you?",
        "What would it look like to take responsibility without taking the blame?",
        "Who else is involved in this situation, and what is their share of the burden?"
    ]),
    # 47. Meaning / Purpose
    (r"(.*) meaning (.*)|(.*) purpose (.*)", [
        "What makes life feel meaningful to you, even in the hard times?",
        "Are you searching for a purpose, or are you creating one?",
        "What's one small thing you did today that added meaning to someone else's life?"
    ]),
    # 48. Identity
    (r"(.*) who am i(.*)|(.*) identity(.*)", [
        "Identity is a journey, not a destination. Who are you becoming?",
        "If you stripped away your job and your roles, what would be left at the core?",
        "What's one part of your identity that you're proud of?"
    ]),
    # 49. Problems
    (r"(.*) problem (.*)|(.*) issue (.*)", [
        "If we treated this problem as a teacher, what is it trying to show you?",
        "What's one part of this issue that is actually within your control?",
        "How has dealing with this problem made you stronger, even if it doesn't feel like it yet?"
    ]),
    # 50. Default / Catch-all
    (r"(.*)", [
        "I hear you. Can you tell me more about that?",
        "How does that sit with you right now?",
        "That sounds like it has a lot of meaning. Could you elaborate?",
        "I'm listening. Please, go on.",
        "What thoughts come up as you say that?",
        "If you could put a feeling to that, what would it be?",
        "Help me understand that from your perspective."
    ])
]

def MAHAHA_chat(user_input):
    for pattern, responses in patterns:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            if match.groups():
                # Filter out None and extract the first valid group
                groups = [g for g in match.groups() if g is not None]
                if groups:
                    # Use the first captured group for reflection
                    match_text = groups[0]
                    reflected_text = reflect(match_text)
                    return response.format(reflected_text)
            return response
    return "I'm listening. Can you try to express that in another way?"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    if not user_input:
        return jsonify({"response": "I'm here. Please, share what's on your mind."}), 400
    
    response = MAHAHA_chat(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    # Using port 5001 for the backend
    app.run(debug=True, host='0.0.0.0', port=5001)
