import sys
# Κάνουμε την "πειρατεία" στη μνήμη με το TurboQuant
import turboquant.integration.vllm 

# Φορτώνουμε τον επίσημο server του vLLM
from vllm.entrypoints.openai.api_server import main

if __name__ == "__main__":
    # Ξεκινάει ο server και περιμένει εντολές από το GPUStack
    main()
