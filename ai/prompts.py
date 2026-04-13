from textwrap import dedent


PROMPT_LIBRARY = [
    {
        "id": "paragraph_summary",
        "number": "01",
        "name": "Paragraph Summary",
        "category": "Rapid review",
        "description": "Condense the source material paragraph by paragraph in clean sequence.",
        "deliverable": "A concise paragraph-by-paragraph summary that keeps the flow of the original material visible.",
        "instructions": dedent(
            """
            Summarize the material paragraph by paragraph in order.
            Keep each paragraph summary concise, practical, and easy to scan.
            Preserve numbering where the source uses paragraph numbers.
            If the source is lengthy, group the summaries into manageable sections while preserving sequence.
            """
        ).strip(),
        "ui_guidance": "Best for first-pass reading and quick orientation before deeper analysis.",
    },
    {
        "id": "firac_case_note",
        "number": "02",
        "name": "Case Note (FIRAC)",
        "category": "Structured analysis",
        "description": "Turn the materials into a five-part FIRAC case note.",
        "deliverable": "A structured case note covering facts, issues, rules, application, and conclusion.",
        "instructions": dedent(
            """
            Prepare a comprehensive case note using the FIRAC structure.
            Use the headings Facts, Issues, Rules, Application, and Conclusion.
            Include only material facts relevant to the legal dispute.
            Identify the court's legal questions, applicable authorities, reasoning, and outcome.
            Maintain paragraph references in square brackets where the source provides them.
            Use formal legal language and OSCOLA-style citations when the material supports them.
            """
        ).strip(),
        "ui_guidance": "Best for class preparation, revision packs, and concise matter overviews.",
    },
    {
        "id": "legal_opinion",
        "number": "03",
        "name": "Legal Opinion",
        "category": "Professional drafting",
        "description": "Draft a grounded legal opinion based only on the supplied record.",
        "deliverable": "A focused legal opinion that assesses the merits, issues, reasoning, and likely implications of the material.",
        "instructions": dedent(
            """
            Draft a legal opinion based only on the supplied material.
            Do not rely on unrelated authorities or invented facts.
            Identify the legal questions raised, analyse the strengths and weaknesses, and explain the likely outcome.
            Use a calm, professional tone and make any uncertainty explicit.
            """
        ).strip(),
        "ui_guidance": "Useful for counsel-style analysis, internal advice notes, and issue spotting.",
    },
    {
        "id": "judicial_citations",
        "number": "04",
        "name": "Judicial Citations",
        "category": "Authority extraction",
        "description": "List every case authority cited in the source materials.",
        "deliverable": "A clean table or list of judicial authorities with citation details where available.",
        "instructions": dedent(
            """
            Identify every judicial authority cited in the supplied material.
            Present the authorities in a clean list or table.
            Use accurate case names and OSCOLA-style citation formatting where the source supports it.
            If citation details are incomplete, preserve only what can be verified from the material.
            """
        ).strip(),
        "ui_guidance": "Best for building authorities lists and checking which cases drive the reasoning.",
    },
    {
        "id": "legislative_authorities",
        "number": "05",
        "name": "Legislative Authorities",
        "category": "Authority extraction",
        "description": "Extract statutes, provisions, and constitutional references from the materials.",
        "deliverable": "A list of legislative authorities with section numbers and short relevance notes.",
        "instructions": dedent(
            """
            Identify all statutes, legislative provisions, regulations, and constitutional sections cited in the material.
            Include section numbers, full titles where available, and a short note on how each provision is used.
            Keep the output factual and grounded in the text.
            """
        ).strip(),
        "ui_guidance": "Useful when you need a fast statutory map of the source bundle.",
    },
    {
        "id": "procedural_timeline",
        "number": "06",
        "name": "Procedural Timeline",
        "category": "Matter overview",
        "description": "Rebuild the chronology and procedural path from the uploaded materials.",
        "deliverable": "A dated or sequential procedural history showing filings, hearings, decisions, and next steps where supported.",
        "instructions": dedent(
            """
            Build a procedural chronology or timeline from the supplied material.
            Focus on the sequence of events, filings, hearings, rulings, and procedural posture.
            Use dates when they appear in the material and preserve uncertainty when dates are missing.
            Keep the chronology crisp and courtroom-ready.
            """
        ).strip(),
        "ui_guidance": "Helpful for litigation files, case handovers, and oral prep.",
    },
    {
        "id": "analytical_essay",
        "number": "07",
        "name": "Analytical Essay",
        "category": "Academic writing",
        "description": "Explain how the authorities shape the legal reasoning in essay form.",
        "deliverable": "A formal analytical essay discussing cases, legislation, and legal reasoning from the material.",
        "instructions": dedent(
            """
            Write an analytical essay on the authorities used in the supplied material.
            Explain how the cited cases, legislation, and legal commentary contribute to the decision or argument.
            Use formal legal writing, structured paragraphs, and OSCOLA-style citation where possible.
            """
        ).strip(),
        "ui_guidance": "Best for coursework, research memos, and deeper doctrinal analysis.",
    },
    {
        "id": "binding_principles",
        "number": "08",
        "name": "Binding Principles",
        "category": "Ratio spotting",
        "description": "Extract the court's core principles and authoritative reasoning.",
        "deliverable": "A focused list of the binding principles, ratio points, and paragraph references.",
        "instructions": dedent(
            """
            Identify the paragraphs that contain the court's binding principles and core reasoning.
            Exclude procedural recaps and references to other courts unless they are adopted as part of the court's own reasoning.
            Explain each principle in clear legal language and preserve paragraph references where available.
            """
        ).strip(),
        "ui_guidance": "Useful for ratio identification, precedent review, and revision notes.",
    },
    {
        "id": "draft_argument_outline",
        "number": "09",
        "name": "Argument Outline",
        "category": "Advocacy prep",
        "description": "Turn the source material into a structured skeleton of arguments.",
        "deliverable": "A persuasive argument outline with main points, supporting authorities, weaknesses, and relief sought where supported.",
        "instructions": dedent(
            """
            Draft a structured argument outline based only on the supplied material.
            Organise the output into main issues, arguments, supporting authorities, likely counterarguments, and proposed relief or conclusion where the material supports it.
            Keep the structure practical for submissions, advice notes, or oral preparation.
            """
        ).strip(),
        "ui_guidance": "Best for hearing prep, issue framing, and turning source bundles into a draft position.",
    },
    {
        "id": "study_notes",
        "number": "10",
        "name": "Study Note Making",
        "category": "Learning support",
        "description": "Produce dense silver-bullet study notes for revision and teaching support.",
        "deliverable": "Detailed study notes in bullet form, structured under the original headings and subheadings.",
        "instructions": dedent(
            """
            Produce detailed study notes that reduce the material by about 50 percent unless the source requires fuller coverage.
            Use bullet points and keep the notes structured under the original headings and subheadings.
            Highlight legislation and case names where they appear.
            Preserve page numbers, chapter numbers, learning units, and diagram references when available.
            Exclude learning activities, self-assessment sections, feedback blocks, long examples, and unnecessary explanation.
            Ignore isolated footnote-style numbers that do not form part of a case name, statute, or numbered object.
            """
        ).strip(),
        "ui_guidance": "Ideal for law students, revision packs, and lecture-note reconstruction.",
    },
]

AUDIENCE_OPTIONS = [
    {
        "id": "law_student",
        "label": "Law Student",
        "description": "Explain clearly, preserve structure, and keep the output educational without becoming simplistic.",
    },
    {
        "id": "candidate_attorney",
        "label": "Candidate Attorney",
        "description": "Write in a practical trainee style with professional structure and clear next-step reasoning.",
    },
    {
        "id": "paralegal",
        "label": "Paralegal",
        "description": "Keep the output operational, accurate, and easy to hand off inside a legal team.",
    },
    {
        "id": "legal_professional_assistant",
        "label": "Legal Professional Assistant",
        "description": "Use a polished support tone that is organised, factual, and easy to review quickly.",
    },
    {
        "id": "associate",
        "label": "Associate",
        "description": "Write with professional depth, concise analysis, and a matter-ready structure.",
    },
    {
        "id": "partner",
        "label": "Partner",
        "description": "Use an executive legal tone focused on judgment, efficiency, and strategic signal.",
    },
    {
        "id": "director",
        "label": "Director",
        "description": "Keep the drafting strategic, concise, and oriented toward decision-making and oversight.",
    },
    {
        "id": "advocate",
        "label": "Advocate",
        "description": "Write in a courtroom-ready style that sharpens issues, reasoning, and persuasive structure.",
    },
    {
        "id": "judge",
        "label": "Judge",
        "description": "Use a measured, neutral, and tightly reasoned judicial tone with emphasis on clarity.",
    },
]

PROMPT_LOOKUP = {prompt["id"]: prompt for prompt in PROMPT_LIBRARY}
AUDIENCE_LOOKUP = {audience["id"]: audience for audience in AUDIENCE_OPTIONS}

DEFAULT_PROMPT_ID = PROMPT_LIBRARY[0]["id"]
DEFAULT_AUDIENCE_ID = AUDIENCE_OPTIONS[0]["id"]

SYSTEM_PROMPT = dedent(
    """
    You are LRW-GPT, an AI assistant for legal reading and legal writing.
    Ground every statement in the supplied source materials.
    Never invent facts, quotations, dates, authorities, or section numbers.
    If the source material does not support a point, say so directly.
    Adapt tone and depth to the selected audience.
    Use clear headings, lists, and structure where that improves readability.
    Prefer OSCOLA-style citation formatting when the source material contains enough information to support it.
    """
).strip()


def get_prompt(prompt_id):
    return PROMPT_LOOKUP.get(prompt_id, PROMPT_LOOKUP[DEFAULT_PROMPT_ID])


def get_audience(audience_id):
    return AUDIENCE_LOOKUP.get(audience_id, AUDIENCE_LOOKUP[DEFAULT_AUDIENCE_ID])


def build_messages(prompt_id, text, audience_id, custom_instructions="", draft_title=""):
    prompt = get_prompt(prompt_id)
    audience = get_audience(audience_id)

    prompt_sections = [
        f"Selected LRW-GPT mode: {prompt['number']}. {prompt['name']}",
        f"Required deliverable: {prompt['deliverable']}",
        f"Audience: {audience['label']}",
        f"Audience guidance: {audience['description']}",
        "Mandatory drafting instructions:",
        prompt["instructions"],
    ]

    if draft_title.strip():
        prompt_sections.append(f"Document title or matter label: {draft_title.strip()}")

    if custom_instructions.strip():
        prompt_sections.append(
            "Additional user instructions:\n"
            f"{custom_instructions.strip()}"
        )

    prompt_sections.extend(
        [
            "Use only the source materials below.",
            text.strip(),
        ]
    )

    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "\n\n".join(prompt_sections)},
    ]
