def generate_template_text(x: int, y: str, z: float) -> str:
    return '{1} is {0} at {2}'.format(x,y,z)

print(generate_template_text(x=12,y="temperature", z=22.4))