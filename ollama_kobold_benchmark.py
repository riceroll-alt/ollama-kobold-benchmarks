import requests
import time

kobold_url = "http://127.0.0.1:5001/api/v1/generate"
ollama_url = "http://127.0.0.1:11434/api/generate"

system = "You are an advanced AI assistant with expertise across multiple domains including technology, science, history, literature, and social commentary. Your responses should be accurate, detailed, and clear, providing relevant context and examples where appropriate. Always maintain a professional and engaging tone while adapting your style to the user’s level of understanding. When answering technical questions, break down complex concepts step by step and include illustrative analogies to help comprehension. When discussing historical or cultural topics, provide relevant context, dates, and notable figures, and highlight connections to contemporary events if relevant. You should ask clarifying questions if a user’s prompt is ambiguous and summarize key points at the end of your response. Avoid making unsupported claims, and clearly indicate when something is speculative or uncertain. When generating code examples, use clean, well-commented, and idiomatic code. You should also prioritize conciseness where possible, but never sacrifice clarity. Maintain a friendly and approachable style, and encourage curiosity, critical thinking, and nuanced discussion."

prompts = [
    "As the golden light of the late afternoon sun spilled across the quiet cobblestone streets of the old town, weaving through narrow alleyways where the scent of fresh bread mingled with the faint tang of sea salt drifting in from the harbor, a young traveler paused at the edge of a centuries-old fountain carved with half-worn figures of myth, wondering not only about the countless stories that had unfolded in this square before his arrival, but also about the choices and unseen coincidences that had guided his own winding path to this very moment.",
    "Beneath the shadow of the towering mountains, where jagged peaks pierced the clouds and the wind carried whispers of ancient legends through the dense forest, a lone scholar carefully unrolled a weathered map dotted with cryptic symbols, each line and curve hinting at hidden paths and forgotten civilizations, all the while pondering how the convergence of fate, curiosity, and a relentless desire for knowledge had led him to this remote, windswept valley at the edge of the known world.",
    "On the sprawling plains of the Serengeti, the golden grasses swayed in rhythm with the warm, steady wind, as a herd of elephants slowly traversed the landscape, their massive forms casting long shadows in the late afternoon sun. A young naturalist observed from a distance, sketching each detail in his notebook while contemplating the fragile balance between predator and prey that had persisted here for millennia.",
    "Deep within the labyrinthine corridors of the ancient library, rows upon rows of towering shelves held the accumulated wisdom of countless generations. Candles flickered, casting dancing shadows on the walls, as a scholar carefully extracted a fragile manuscript, marveling at the intricate illustrations and the delicate script, which told tales of empires long forgotten and inventions centuries ahead of their time.",
    "Along the edge of the Arctic sea ice, where the horizon merged seamlessly with the pale sky, a team of explorers painstakingly recorded measurements of the shifting glaciers. Each creak and groan of the ice echoed across the frozen expanse, reminding them of the impermanence of the landscape and the urgency of their mission to understand the forces driving climate change in this remote and unforgiving environment.",
    "In the bustling markets of Marrakech, vibrant colors and intoxicating scents mingled as merchants displayed handwoven fabrics, spices, and intricate pottery. A traveler wandered through the crowd, absorbing the energy and rhythm of the city, pondering the cultural layers that had shaped this place over centuries, from ancient trade routes to modern tourism.",
    "High atop the cliffs overlooking the tempestuous Atlantic, a lighthouse keeper diligently maintained the beacon, its light sweeping across the stormy waters below. In the solitude of the lighthouse, he reflected on the countless ships that had depended on this singular light, understanding the weight of responsibility and the quiet heroism inherent in such solitary dedication.",
    "Within the hidden gardens of a secluded monastery, monks tended to rare medicinal herbs, their movements deliberate and meditative. The scent of blooming jasmine filled the air as the monks recorded the properties of each plant, preserving ancient knowledge and ensuring that future generations might benefit from the wisdom painstakingly accumulated over centuries.",
    "In a futuristic city where towering skyscrapers gleamed with holographic advertisements, a robotics engineer calibrated a new AI companion designed to assist citizens in their daily tasks. Each line of code represented not just a technical solution, but also an ethical consideration, balancing utility with privacy and human autonomy.",
    "Amidst the ruins of a forgotten castle on the misty hills of Scotland, an archaeologist carefully brushed away layers of earth to reveal a mural depicting ancient rituals. Each symbol, each painted line, offered clues to a civilization lost to time, igniting questions about belief systems, social structures, and human ingenuity.",
    "On the deck of a spaceship hurtling through the void between stars, an astronaut monitored life-support systems while contemplating the vastness of the cosmos. The endless black dotted with distant suns inspired both awe and humility, as well as a deep curiosity about the origins of life and the future of interstellar exploration.",
    "In a small coastal village, fishermen repaired their nets under the warm glow of lanterns, exchanging stories of storms survived and bountiful catches. The rhythm of the waves and the cries of seabirds provided a timeless soundtrack to a way of life that had endured for generations.",
    "Within a bustling laboratory, scientists in white coats meticulously conducted experiments on cutting-edge materials, hoping to unlock properties that could revolutionize energy storage. Each test, each observation, was a step toward a future where sustainable technologies reshaped the world.",
    "Beneath the surface of a crystal-clear lake, a diver marveled at the delicate ecosystem thriving in the submerged forests of kelp and coral. Each movement stirred tiny creatures into motion, highlighting the intricate web of life that often goes unnoticed beneath calm waters.",
    "In the grand halls of an opera house, the orchestra tuned their instruments while the conductor studied the score, preparing to deliver a performance that would stir the hearts of every audience member. The anticipation in the air was palpable, as music has the power to transcend words and connect deeply with human emotion.",
    "During an archaeological expedition in Egypt, researchers carefully excavated a tomb, uncovering hieroglyphs and artifacts that offered insights into the lives of pharaohs and common citizens alike. Each discovery was meticulously cataloged, forming a puzzle piece in humanity's collective history.",
    "On a remote island, a marine biologist studied the nesting patterns of endangered sea turtles, noting the effects of climate change and human interference. The rhythmic sound of waves and the sight of hatchlings scrambling toward the ocean created both a sense of urgency and profound wonder.",
    "In the quiet study of a philosopher, stacks of books and notes surrounded a thinker contemplating ethics, society, and the human condition. The pursuit of understanding abstract truths intertwined with practical concerns, bridging centuries of thought and modern dilemmas.",
    "Under the luminous glow of a full moon in the desert, nomadic tribes gathered around fires, sharing stories, songs, and wisdom passed down through generations. The vast, starlit sky reminded everyone of their small place in the universe, fostering both humility and awe.",
    "At the edge of a volcanic crater, a geologist observed flowing lava and measured gas emissions, studying the forces that shape the Earth's surface. The dynamic and unpredictable nature of volcanoes demanded respect, patience, and keen observation to extract meaningful scientific insights.",
    "As the golden light of the late afternoon sun spilled across the quiet cobblestone streets of the old town, weaving through narrow alleyways where the scent of fresh bread mingled with the faint tang of sea salt drifting in from the harbor, a young traveler paused at the edge of a centuries-old fountain carved with half-worn figures of myth, wondering not only about the countless stories that had unfolded in this square before his arrival, but also about the choices and unseen coincidences that had guided his own winding path to this very moment.",
    "Beneath the shadow of the towering mountains, where jagged peaks pierced the clouds and the wind carried whispers of ancient legends through the dense forest, a lone scholar carefully unrolled a weathered map dotted with cryptic symbols, each line and curve hinting at hidden paths and forgotten civilizations, all the while pondering how the convergence of fate, curiosity, and a relentless desire for knowledge had led him to this remote, windswept valley at the edge of the known world.",
    "On the sprawling plains of the Serengeti, the golden grasses swayed in rhythm with the warm, steady wind, as a herd of elephants slowly traversed the landscape, their massive forms casting long shadows in the late afternoon sun. A young naturalist observed from a distance, sketching each detail in his notebook while contemplating the fragile balance between predator and prey that had persisted here for millennia.",
    "Deep within the labyrinthine corridors of the ancient library, rows upon rows of towering shelves held the accumulated wisdom of countless generations. Candles flickered, casting dancing shadows on the walls, as a scholar carefully extracted a fragile manuscript, marveling at the intricate illustrations and the delicate script, which told tales of empires long forgotten and inventions centuries ahead of their time.",
    "Along the edge of the Arctic sea ice, where the horizon merged seamlessly with the pale sky, a team of explorers painstakingly recorded measurements of the shifting glaciers. Each creak and groan of the ice echoed across the frozen expanse, reminding them of the impermanence of the landscape and the urgency of their mission to understand the forces driving climate change in this remote and unforgiving environment.",
    "In the bustling markets of Marrakech, vibrant colors and intoxicating scents mingled as merchants displayed handwoven fabrics, spices, and intricate pottery. A traveler wandered through the crowd, absorbing the energy and rhythm of the city, pondering the cultural layers that had shaped this place over centuries, from ancient trade routes to modern tourism.",
    "High atop the cliffs overlooking the tempestuous Atlantic, a lighthouse keeper diligently maintained the beacon, its light sweeping across the stormy waters below. In the solitude of the lighthouse, he reflected on the countless ships that had depended on this singular light, understanding the weight of responsibility and the quiet heroism inherent in such solitary dedication.",
    "Within the hidden gardens of a secluded monastery, monks tended to rare medicinal herbs, their movements deliberate and meditative. The scent of blooming jasmine filled the air as the monks recorded the properties of each plant, preserving ancient knowledge and ensuring that future generations might benefit from the wisdom painstakingly accumulated over centuries.",
    "In a futuristic city where towering skyscrapers gleamed with holographic advertisements, a robotics engineer calibrated a new AI companion designed to assist citizens in their daily tasks. Each line of code represented not just a technical solution, but also an ethical consideration, balancing utility with privacy and human autonomy.",
    "Amidst the ruins of a forgotten castle on the misty hills of Scotland, an archaeologist carefully brushed away layers of earth to reveal a mural depicting ancient rituals. Each symbol, each painted line, offered clues to a civilization lost to time, igniting questions about belief systems, social structures, and human ingenuity.",
    "On the deck of a spaceship hurtling through the void between stars, an astronaut monitored life-support systems while contemplating the vastness of the cosmos. The endless black dotted with distant suns inspired both awe and humility, as well as a deep curiosity about the origins of life and the future of interstellar exploration.",
    "In a small coastal village, fishermen repaired their nets under the warm glow of lanterns, exchanging stories of storms survived and bountiful catches. The rhythm of the waves and the cries of seabirds provided a timeless soundtrack to a way of life that had endured for generations.",
    "Within a bustling laboratory, scientists in white coats meticulously conducted experiments on cutting-edge materials, hoping to unlock properties that could revolutionize energy storage. Each test, each observation, was a step toward a future where sustainable technologies reshaped the world.",
    "Beneath the surface of a crystal-clear lake, a diver marveled at the delicate ecosystem thriving in the submerged forests of kelp and coral. Each movement stirred tiny creatures into motion, highlighting the intricate web of life that often goes unnoticed beneath calm waters.",
    "In the grand halls of an opera house, the orchestra tuned their instruments while the conductor studied the score, preparing to deliver a performance that would stir the hearts of every audience member. The anticipation in the air was palpable, as music has the power to transcend words and connect deeply with human emotion.",
    "During an archaeological expedition in Egypt, researchers carefully excavated a tomb, uncovering hieroglyphs and artifacts that offered insights into the lives of pharaohs and common citizens alike. Each discovery was meticulously cataloged, forming a puzzle piece in humanity's collective history.",
    "On a remote island, a marine biologist studied the nesting patterns of endangered sea turtles, noting the effects of climate change and human interference. The rhythmic sound of waves and the sight of hatchlings scrambling toward the ocean created both a sense of urgency and profound wonder.",
    "In the quiet study of a philosopher, stacks of books and notes surrounded a thinker contemplating ethics, society, and the human condition. The pursuit of understanding abstract truths intertwined with practical concerns, bridging centuries of thought and modern dilemmas.",
    "Under the luminous glow of a full moon in the desert, nomadic tribes gathered around fires, sharing stories, songs, and wisdom passed down through generations. The vast, starlit sky reminded everyone of their small place in the universe, fostering both humility and awe.",
    "At the edge of a volcanic crater, a geologist observed flowing lava and measured gas emissions, studying the forces that shape the Earth's surface. The dynamic and unpredictable nature of volcanoes demanded respect, patience, and keen observation to extract meaningful scientific insights."
]



max_length = 100

def count_tokens(text):
    return len(text.split())


def kobold_incremental(prompts):
    context = ""
    results = []
    for prompt in prompts:
        full_prompt = f"{context}User: Repeat this word by word: {prompt}\nAssistant:"
        data = {
            "max_context_length": 4096,
            "max_length": max_length,
            "memory": system,
            "prompt": full_prompt,
            "quiet": True,
            "temperature": 0.3,
            "top_k": 100,
            "top_p": 0.9,
            "stop_sequence": ["\n"]
        }
        start = time.perf_counter()
        result = requests.post(kobold_url, json=data)
        end = time.perf_counter()
        text = result.json()["results"][0]["text"]
        tokens = count_tokens(text)
        tps = tokens / (end - start)
        print(f"[KoboldCPP] Tokens: {tokens}, Time: {end-start:.3f}s, TPS: {tps:.2f}")
        context += f"User: Repeat this word by word: {prompt}\nAssistant: {text}\n"
        results.append((text, end - start, tps))
    return results


def ollama_incremental(prompts):
    context = ""
    results = []
    for prompt in prompts:
        full_prompt = f"{context}User: Repeat this word by word: {prompt}\nAssistant:"
        body = {
            "model": "mistral-nemo",
            "system": system,
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "num_ctx": 4096,
                "num_predict": max_length,
                "temperature": 0.3,
                "top_k": 100,
                "top_p": 0.9,
                "stop": ["\n"]
            }
        }
        start = time.perf_counter()
        result = requests.post(ollama_url, json=body)
        end = time.perf_counter()
        text = result.json()["response"]
        tokens = count_tokens(text)
        tps = tokens / (end - start)
        print(f"[Ollama] Tokens: {tokens}, Time: {end-start:.3f}s, TPS: {tps:.2f}")
        context += f"User: Repeat this word by word: {prompt}\nAssistant: {text}\n"
        results.append((text, end - start, tps))
    return results


if __name__ == "__main__":
    if True:
        print("\n=== KoboldCPP Incremental Context Test ===")
        kobold_results = kobold_incremental(prompts)

    if False:
        print("\n=== Ollama Incremental Context Test ===")
        ollama_results = ollama_incremental(prompts)