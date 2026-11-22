#!/usr/bin/env python3
"""
AI Portfolio Helper
Small utility for generating and refining portfolio content.
Developed with AI assistance for COSC 4272.
"""

import textwrap
from datetime import datetime

def generate_about_me(name="Yves Bail", major="Computer Game Development", school="Lamar University"):
    draft = f"""
I am a {major} student at {school} with a focus on 3D graphics, interactive systems, and practical software development. 
Through coursework in C++, LightWave 3D, computer architecture, and Android development, I have gained hands-on experience 
building and debugging technical projects. I regularly use AI-assisted tools to accelerate prototyping and improve code quality 
while maintaining careful review of all generated suggestions. I am preparing for roles in software development and game-related 
engineering where I can contribute clean, documented solutions and continue growing as a professional developer.
    """.strip()
    return textwrap.fill(draft, width=80)

def improve_project_description(title, raw_desc):
    improved = f"**{title}**\n\n{raw_desc.strip()}\n\nKey improvements suggested: clearer technologies list, measurable outcomes, and professional tone."
    return improved

def skills_gap_checklist():
    items = [
        "Strengthen cloud fundamentals (AWS or Azure basics)",
        "Add one deployed web project with GitHub Pages or Vercel",
        "Document 2–3 projects with screenshots and clear READMEs",
        "Practice technical interview questions (algorithms + system design basics)",
        "Update LinkedIn and GitHub profile consistently"
    ]
    return "\n".join(f"- [ ] {item}" for item in items)

def main():
    print("=== AI Portfolio Helper ===\n")
    print("1. About Me Draft")
    print(generate_about_me())
    print("\n" + "="*50 + "\n")
    print("2. Sample Project Improvement")
    print(improve_project_description(
        "LightWave Farm Scene",
        "Created a textured 3D farm environment with animated windmill, house, barn, and trees."
    ))
    print("\n" + "="*50 + "\n")
    print("3. Skills Gap Checklist")
    print(skills_gap_checklist())
    print(f"\nGenerated on {datetime.now().strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
