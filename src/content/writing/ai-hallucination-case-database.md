---
title: "1,356 Cases: Publishing the AI Hallucination Legal Database"
description: "We've been tracking every court proceeding where generative AI produced fabricated citations, invented quotes, or misrepresented legal authorities. The full dataset is now public."
publishedAt: 2026-05-19
draft: true
---

For the past two years, we have been documenting every case we could find where generative AI produced hallucinated content in a legal proceeding — fabricated citations, invented quotes, cases that don't exist, statutes that were never passed, holdings that say the opposite of what the AI claimed.

The database now has 1,356 entries across 34 jurisdictions. Today we're making the full dataset public.

**What's in it.** Each entry records the case name and court, the date, which party submitted the AI-generated content, the specific AI tool used, the type of hallucination, the outcome, and any monetary or professional sanction. The entries span US federal and state courts, international tribunals, and arbitration proceedings. The earliest case is from April 2023. The most recent is from April 2026.

**Why it matters.** The standard narrative around AI hallucination in law treats each incident as isolated — a single attorney who didn't check their citations, an embarrassing footnote, a one-time problem now solved by better prompting habits. The database tells a different story. Across 1,356 cases, the failure modes are consistent, the tools involved are varied, and the outcomes range from brief judicial reprimands to five-figure sanctions to dismissed cases. This is a systematic pattern, not a rounding error.

**What the pattern looks like.** Citation fabrication is the most common category — cases and statutes that simply do not exist, presented with the same surface confidence as real authority. Quote fabrication is the second: the underlying case exists, but the language attributed to the court does not appear in the actual opinion. Holding misrepresentation — real cases cited for propositions they don't support — is subtler and harder to catch without pulling the original. These three categories account for the majority of sanctions.

**The tools involved are not obscure.** The database includes incidents involving the major legal research platforms — LexisNexis, Westlaw, Casetext — as well as general-purpose models used directly. The hallucination problem is not limited to attorneys using consumer AI tools outside their intended context. It appears throughout the stack.

**The dataset is available for research.** The full structured data is downloadable as JSON from the [AI Hallucination Cases](/AI-legal-research) page, licensed CC BY 4.0. Fields include court, jurisdiction, date, party, AI tool, hallucination category, outcome, and source URL for the underlying court document. Researchers, law professors, and legal technologists are welcome to use it with attribution.

**The citation format:** Kameir, Christian. *AI Hallucination Cases in Legal Proceedings*. Decentralized Publishing LLC. https://kameir.com/AI-legal-research

**What this underpins.** The database is the factual foundation for *Ethics-Safe AI Use for Law Firms* and the [6-hour CLE course](/AI-Ethics-CLE-Course-Sample) built from it. The course is the only CLE program built directly from the sanctions record rather than from hypotheticals or vendor documentation. Every module is grounded in cases that actually happened.

The database is updated as new cases are reported. If you are aware of a case that should be included, the contact page has a form.
