class CouncilService:

    def __init__(
        self,
        llm_service,
        prompt_service,
        retrieval_service,
        embedding_service,
        brahma_service
    ):
        self.llm_service = llm_service
        self.prompt_service = prompt_service
        self.retrieval_service = retrieval_service
        self.embedding_service = embedding_service
        self.brahma_service = brahma_service

        self.deities = [
            "Krishna",
            "Shiva",
            "Asura"
        ]

    def conduct_council(self, question):

        judgments = []

        query_embedding = self.embedding_service.create_embeddings(
            [question]
        )

        for deity in self.deities:

            results = self.retrieval_service.search(
                query_embedding,
                top_k=3,
                deity=deity
            )

            prompt = self.prompt_service.build_prompt(
                question,
                results,
                deity
            )

            response = self.llm_service.generate_response(prompt)

            judgments.append({
                "deity": deity,
                "response": response
            })

        final_judgment = self.brahma_service.calculate_final_judgment(
            question,
            judgments
        )

        return {
            "judgments": judgments,
            "final_judgment": final_judgment
        }