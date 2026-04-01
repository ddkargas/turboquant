# 1. Ξεκινάμε από το έτοιμο, επίσημο vLLM
FROM vllm/vllm-openai:v0.18.0

# 2. Απενεργοποιούμε τον αυστηρό έλεγχο έκδοσης CUDA της Nvidia
ENV NVIDIA_DISABLE_REQUIRE=1

# 2. Ορίζουμε το φάκελο εργασίας
WORKDIR /workspace/turboquant

# 3. Αντιγράφουμε ΟΛΑ τα αρχεία από το δικό σου GitHub μέσα στην εικόνα (μαζί και το start_server.py)
COPY . .

# 4. Εγκαθιστούμε το TurboQuant σαν plugin
RUN pip install -e .

# 5. Ορίζουμε να ξεκινάει πάντα με το δικό μας script
ENTRYPOINT ["python3", "start_server.py"]
