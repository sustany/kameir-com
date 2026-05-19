---
title: "AI Hallucinations in Legal Research: What Actually Goes Wrong and How to Catch It"
description: "Not all AI errors in legal research are the same. A five-category taxonomy explains how hallucinations differ from citation errors, and what verification step catches each."
publishedAt: 2026-05-19
draft: false
---

The lawyers sanctioned for AI-generated filings were not, in most cases, reckless people. They were busy people who used a tool that looked like it was working — until it wasn't. The problem with AI hallucinations in legal research is not that they are obvious. It is that they are not.

Understanding what actually goes wrong, and why, is the foundation of any reasonable verification practice.

## Five types of error — not one

"Hallucination" is a catch-all that obscures important differences. In analyzing over 1,350 cases from the [AI Legal Research Case Database](/AI-legal-research), five distinct failure modes emerge — and each requires a different corrective.

**Fabricated authority.** The model invents a case, statute, or regulation that does not exist. The citation has a plausible form — correct court, plausible year, realistic parties — but there is nothing at that citation. This is the failure mode that generated the Mata sanctions and most of the earliest high-profile disciplinary referrals. Verification: run every citation against Westlaw, Lexis, or the relevant court docket before filing.

**False quotation.** The case exists, but the language attributed to it does not appear in that opinion. The model has synthesized language that reflects the court's apparent reasoning but is not what the court actually said. This failure mode is more dangerous than fabrication in some ways: the citation checks out, so a lawyer who stops at verifying the citation has not caught the error. Verification: pull the actual opinion and confirm the quoted language verbatim.

**Misrepresented holding.** The case exists, the language is real, but the proposition for which it is cited is wrong. The model has characterized the holding in a way that does not reflect what the court decided — sometimes because it has confused the holding with dictum, sometimes because it has conflated a dissent with the majority opinion, sometimes because the case was subsequently limited or distinguished. Verification: read the headnotes and the actual holding section; check subsequent history.

**Outdated authority.** The rule stated was accurate at some point but is no longer good law. The model's training data has a cutoff, and it cannot know about subsequent legislative changes, regulatory amendments, or cases that overruled or distinguished the cited authority. This is structurally not a hallucination in the strict sense — the model is not inventing — but the practical effect on a filing is the same. Verification: check current status through KeyCite or Shepard's.

**Incomplete disclosure.** The model produces research that is technically accurate but omits material adverse authority. This is the subtlest category because it produces no affirmative error — it simply leaves out what a competent researcher would have found. Verification: run independent searches across multiple tools and databases, not just the AI's output.

## Why verification protocol matters more than tool selection

A recurring pattern in sanctioned filings is that lawyers who used AI verification tools to check AI-generated research were not protected. A large language model used to verify output from another large language model tends to replicate the same omissions and errors — the models draw on similar training data and have similar blind spots.

The verification that courts appear to expect — and that ABA Opinion 512 grounds in existing competence and candor obligations — is independent verification against primary sources. Not AI-checking AI.

This matters practically for how training is designed. A CLE course that teaches lawyers to use tool B to check tool A has not trained lawyers to verify. It has trained lawyers to feel verified. The [AI Ethics training program](/ai-ethics-training) at issue here is structured specifically around this distinction: what it means to have a verification step, not just to have performed some act that resembles one.

## The supervision question

ABA Opinion 512 applies the existing supervisory rules — 5.1 and 5.3 — to AI use. This means that a supervising attorney who reviews AI-assisted work product for substance but does not independently verify citations may have a supervision problem even if the substantive review was thorough.

The logic follows from Rule 5.1(b): a supervising lawyer must make reasonable efforts to ensure that supervised lawyers' work conforms to the rules. If the supervised lawyer used AI and the supervisor did not have a verification protocol in place, the supervisor's review of the resulting document is not the same as a reasonable effort.

This is not a novel doctrinal argument — it is the straightforward application of existing rules to a new workflow. What makes it feel novel is that the workflow is new, and the specific failure modes of AI are different from the specific failure modes of junior associate research that the supervisory rules were written to address.

## The [Mata Protocol](/ai-ethics/mata-protocol) as a minimum floor

The verification steps required by the Mata Protocol — independently confirm every citation, check subsequent history, verify quoted language against the original opinion — address fabricated authority, outdated authority, and false quotation. They do not by themselves address misrepresented holding or incomplete disclosure.

A complete verification protocol needs to cover all five categories. In practice this means:

1. Confirm existence (every citation resolves to a real document)
2. Confirm currency (subsequent history clean)
3. Confirm quotation (language appears verbatim in the cited source)
4. Confirm holding (the case stands for the proposition cited)
5. Confirm completeness (independent search for adverse authority)

Steps one through three are mechanical and can be partially systematized. Steps four and five require legal judgment and cannot be delegated back to an AI tool.

## What sanctions data shows about failure patterns

Of the 1,356 cases in the database, the largest category involves fabricated authority — invented citations that resolved to nothing. This is partly because fabricated citations are the most visible failure: they get caught when opposing counsel or the court checks. The database almost certainly undercounts false quotations and misrepresented holdings, which require more careful reading to identify.

The trend line in the data is toward monetary sanctions and ongoing disclosure requirements rather than the warnings that characterized the earliest cases. Courts have signaled that the novelty defense — "I didn't know AI could do this" — has a limited shelf life.

---

*The [AI Legal Research Case Database](/AI-legal-research) tracks over 1,356 cases where AI-generated content produced errors in legal proceedings. The [Ethics-Safe AI Use for Law Firms eBook](/ai-ethics-ebook) covers the full verification framework, the five-category taxonomy, and the Model Rules analysis in detail.*
