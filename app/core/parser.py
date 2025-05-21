import config
from packaging.requirements import Requirement


def parse_requirements(requirements: str) -> tuple:
    """
    Parse requirements.txt content and returns a list of tuples
    Skiped dependencies are added to the ignored list
    """
    valid = []
    ignored = []
    for line in requirements.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            req = Requirement(line)
            # Exact version match
            if req.specifier and len(req.specifier) == 1:
                spec = next(iter(req.specifier))
                if spec.operator == "==":
                    valid.append((req.name, spec.version))
                else:
                    ignored.append(line)
            else:
                ignored.append(line)
        except Exception:
            ignored.append(line)

    return valid, ignored
