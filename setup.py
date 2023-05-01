from setuptools import setup

setup(
    name="ouroboros",
    version="0.0.1",
    description="Re-implementation of the self-instruct paper, with updated prompts, models, etc.",
    url="https://github.com/jondurbin/ouroboros",
    author="Jon Durbin",
    license="Apache 2.0",
    packages=["ouroboros"],
    install_requires=[
        "rouge-score>=0.1.2",
        "aiohttp>=3.8",
        "backoff>=2.2",
        "requests>=2.28",
        "loguru>=0.7",
    ],
    extras_require={
        "dev": [
            "black",
            "flake8",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "console_scripts": [
            "ouroboros = ouroboros.entrypoint:run"
        ]
    },
)