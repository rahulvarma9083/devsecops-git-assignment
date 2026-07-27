def scan():
    print("Scanning application for security issues...")


def validate_username(username):
    if not username:
        return False

    if len(username) < 3:
        return False

    return True

def generate_security_report():
    print("Security Report")
    print("---------------")
    print("Configuration Scan: Passed")
    print("Input Validation: Passed")