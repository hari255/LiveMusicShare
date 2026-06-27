                    Mobile App
                        |
                        |
                  FastAPI Gateway
                        |
        --------------------------------
        |              |               |
 Listening API    Discovery API    AI Agent Layer
        |              |               |
        |              |               |
 PostgreSQL       Vector DB        LangGraph
        |              |               |
        |              |               |
 Event Data     Embeddings       RAG + LLM
        |
        |
 Data Pipeline
 (Spark/PubSub)



 ================================================================

                 User Intent

                    |
                    v

        +----------------------+
        | Discovery Agent      |
        +----------------------+

              /       \
             /         \

 Listening History   Nearby Trends

             \         /

              \       /

              Music Search

                    |

              Recommendation