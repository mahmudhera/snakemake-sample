rule run_main:
    input:
        "main.py",
        "README.md"
    output:
        "tmp"
    benchmark:
        "test_benchmark"
    shell:
        "python main.py {input[0]} {output}"
