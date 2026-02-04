import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "1.0.0"


REPO_NAME = "realtime-ppe-safety-monitor"
AUTHOR_USER_NAME = "Arash-Keshavarz"
SRC_REPO = "PPE_DETECTION"
AUTHOR_EMAIL = "arash.keshavarz.dev@gmail.com"

def _read_requirements(path: str = "requirements.txt") -> list[str]:
    reqs: list[str] = []
    try:
        with open(path, "r", encoding="utf-8") as req_file:
            for line in req_file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if line.startswith("-e ") or line == "-e." or line == "-e .":
                    continue
                reqs.append(line)
    except FileNotFoundError:
        pass
    return reqs

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A comprehensive project for detecting PPE safety in real-time using YOLOv26.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.12",
    install_requires=_read_requirements(),
)
    