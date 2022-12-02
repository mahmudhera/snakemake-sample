str = 'test'
rule run_main:
    input:
        "main.py",
        "README.md"
    output:
        "tmp"
    benchmark:
        str + "benchmark"
    shell:
        for i in range(2):
            "python main.py {input[0]} {output}"
