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
        "python main.py {input[0]} {output}"
