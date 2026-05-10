class ConversationMemory:
    def __init__(self):
        self.context = {
            "role": None,
            "skills": [],
            "intent": None,
            "history": []
        }

    def update(self, ai_data: dict, user_message: str):
        if ai_data.get("role"):
            self.context["role"] = ai_data["role"]

        if ai_data.get("skills"):
            self.context["skills"].extend(ai_data["skills"])
            self.context["skills"] = list(set(self.context["skills"]))

        if ai_data.get("intent"):
            self.context["intent"] = ai_data["intent"]

        self.context["history"].append(user_message)

    def get_context(self):
        return self.context