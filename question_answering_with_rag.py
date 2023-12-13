from langchain import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class QuestionAnsweringExperiment:
    """
    This class defines logic to setup an experiment to test how model can answer questions with:
    - plain llm chain. Just an llm and a prompt using langchain.
    - Retrieval augmeneted generation chain - a chain with the access to the external file content.
    """

    def __init__(
        self,
        repo_id: str,
        external_data_path: str,
        embedding_model_name: str,
        plain_lmm_prompt_template: str,
    ):
        self.llm = HuggingFaceHub(
            repo_id=repo_id, model_kwargs={"temperature": 0.05, "max_length": 200}
        )
        self.setup_plain_llm_chain(plain_lmm_prompt_template)

    def setup_plain_llm_chain(self, prompt_template):
        """
        adds an atrtibute self.plain_llm_chain and assigns an LLMChain with self.lmm and given prompt template.
        """
        self.plain_llm_chain = LLMChain(
            llm=self.llm, prompt=PromptTemplate.from_template(prompt_template)
        )

    def init_embedding_model(self, model_name):
        """
        takes as input model_name from HuggingFace and returns an initialised model.
        A model_name can be any decent embedding model from HF. E.g. bert will work,
        but probably one can find better models.
        """
        pass

    def create_vector_database(self, documents, embedding_model):
        """
        creates faiss database, puts documents and embedding model into it.
        Please use Langchain imterfaces to initialise faiss.
        """
        pass

    def load_documents_from_file(self, file_path):
        """
        takes as input a filepath and loads it with the loader from Langchain.
        """
        pass

    def download_prompt_from_hub(self, prompt_name):
        """
        Takes as input any prompt name from langchain hub and downloads it.
        """
        pass

    def setup_rag_llm_chain(self, external_data_path, embedding_model_name):
        """
        1) loads documents into memory
        2) initialised embedding model
        3) creates a failss datavase, puts there documents and passes there embedding model
        4) add attribute self.rag_llm_chain and initialises a QA chain with RAG
        """
        pass

    def predict_with_llm_chain(self, query):
        """
        Takes as input a query and returns generated result.
        Raises AtrributeError if plain_llm_chain attr doesnt exist.
        """
        if not hasattr(self, "plain_llm_chain"):
            raise AttributeError("Please set up a chain before calling predict")
        return self.plain_llm_chain.run(query)

    def predict_with_rag_chain(self, query):
        """
        Takes as input a query and returns generated result.
        Raises AtrributeError if plain_llm_chain attr doesnt exist.
        """
        pass


if __name__ == "__main__":
    """
    Main entrypoint.
    1) Initialises experiment as an instance of QuestionAnsweringExperiment with passed params.
    2) initialises a set of test queries.
    3) iterate queries and runs "predict_with_llm_chain" and "predict_with_rag_chain" methods.
    4) prints results of generated answers for both setups as well as expected result.
    """
    # make sure you set up your token
    # export HUGGINGFACEHUB_API_TOKEN=my_key

    qa_prompt_template = """Answer the question. If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Question: {question}
    Helpful Answer:"""

    experiment = QuestionAnsweringExperiment(
        repo_id="google/flan-t5-large",
        external_data_path="data/cats_content.txt",
        embedding_model_name="update-with-your-model",  # update this
        plain_lmm_prompt_template=qa_prompt_template,
    )

    queries = [
        ("Are cats good jumpers?", "yes"),
        ("How far can cat jump in compare with its own length?", "up to 6 times"),
        ("How many bones does cat have?", "230"),
        ("How many toes does each front paw of a cat has?", "five"),
    ]

    print("\nStarting answering questions! \n")
    for query, answer in queries:
        print(f"{query}, expected answer: {answer} \n")
        plain_llm_answer = experiment.predict_with_llm_chain(query)
        print(f"plain llm answer: {plain_llm_answer} \n")

        """ UNCOMMENT THE CODE BELOW WHEN YOU FINISH 
        AND COMPARE HOW RAG MODEL ANSWERS QUESTIONS """
        # rag_llm_answer = experiment.predict_with_rag_chain(query)
        # print(f"RAG llm answer: {rag_llm_answer} \n")
