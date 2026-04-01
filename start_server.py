import sys
import runpy

# 1. Κάνουμε την "πειρατεία" στη μνήμη (Monkey Patch)
import turboquant.integration.vllm 

if __name__ == "__main__":
    # 2. Διορθώνουμε το όνομα για να μην μπερδευτεί το vLLM με τις παραμέτρους
    sys.argv[0] = "vllm.entrypoints.openai.api_server"
    
    # 3. Ξεκινάμε τον επίσημο server με ασφάλεια
    runpy.run_module("vllm.entrypoints.openai.api_server", run_name="__main__", alter_sys=True)
