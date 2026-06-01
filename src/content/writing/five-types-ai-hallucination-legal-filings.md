---
title: "The Five Types of AI Hallucination in Legal Filings"
description: "Not all AI hallucinations look the same in a legal filing. The five-category taxonomy from Ethics-Safe AI Use for Law Firms maps each failure type to the verification step that catches it."
publishedAt: 2026-05-22
draft: false
---

Most conversations about AI hallucination in legal practice treat it as a single problem: the AI made something up. That framing is too coarse to be useful. Different hallucination types have different causes, different detection methods, and different professional responsibility implications. Treating them as one category means your verification protocol has the wrong shape.

The taxonomy below draws on the framework developed in [Ethics-Safe AI Use for Law Firms](/ai-ethics) and on the patterns documented in the documented court orders and sanctions. Each type is distinct. Each requires a different catch.

## Type 1: Citation Fabrication

The AI generates a case citation for a case that does not exist. The reporter, volume, page number, and court designation are all plausible. The year is plausible. The case name sounds like a real case. None of it is real.

This is the hallucination type that entered public consciousness with Mata v. Avianca in 2023, and it remains the most documented type in sanctions proceedings. It is also the easiest to catch: a citation check against Westlaw, Lexis, or Google Scholar resolves it immediately.

The failure mode is not that the attorney used AI. It is that the attorney treated the AI output as a first draft ready for filing rather than as a starting point requiring verification. Courts have been explicit about this in their sanctions orders. The tool does not know what it does not know. The attorney does.

**The catch:** Every case citation must be verified at a primary source before it enters a filing. No exceptions for deadline pressure.

## Type 2: Attribution Hallucination

The AI correctly identifies a real case but misrepresents what it said. The case exists, can be retrieved, and was decided by the court the AI named. The holding, the quoted language, or the procedural posture is wrong.

This type is more dangerous than citation fabrication precisely because the case exists. An attorney who spots that a case cannot be found will pull the filing. An attorney who confirms the case exists may not read far enough to catch that the holding was inverted.

Attribution hallucination appears in two forms. In the first, the AI summarizes a holding in the attorney's favor when the actual holding went the other way. In the second, the AI generates a quotation that sounds like the court's language but does not appear in the opinion. Both have appeared in documented sanctions cases.

**The catch:** Confirming a case exists is not enough. The holding summary must be checked against the actual opinion, and any quoted language must be located verbatim in the original text.

## Type 3: Statutory and Regulatory Fabrication

The AI generates a reference to a statute, regulation, or agency guidance document that does not exist. It may cite a real code section but describe provisions that are not there, or it may fabricate a section number entirely. In administrative law contexts, it may attribute a policy position to an agency that has no such record.

This hallucination type is underrepresented in sanctions proceedings relative to citation fabrication, not because it occurs less frequently but because it is less likely to be caught by opposing counsel doing a citation check. A fabricated case name is searchable. A fabricated regulatory provision in a dense administrative record is harder to isolate.

**The catch:** Statutory and regulatory citations require the same primary-source verification as case citations. If the AI cites a specific subsection, that subsection needs to be pulled and read. The section number being real does not mean the described content is accurate.

## Type 4: Jurisdictional and Procedural Hallucination

The AI applies the right legal concept to the wrong jurisdiction or procedural context. It may cite federal circuit law in a state court filing, apply an evidentiary standard from one circuit in a different circuit, or describe procedural rules that apply in a different court system.

This type is particularly common when an attorney uses an AI tool for a matter outside their primary practice jurisdiction. The model has learned legal patterns across many jurisdictions and may conflate them. The output sounds authoritative because the underlying concept is real; only the jurisdictional application is wrong.

**The catch:** Any citation or rule description that the drafting attorney could not independently verify from their own practice knowledge should be flagged for a jurisdiction-specific review before filing.

## Type 5: Temporal Hallucination

The AI treats superseded law as current. It cites a case that was valid precedent at the time of the model's training cutoff but has since been reversed, limited, or effectively overruled by subsequent authority. It may also cite a regulation that has been amended or a statute that has been repealed.

Every large language model has a training cutoff. Legal authority changes continuously. A model trained through a given date cannot know about authority issued after that date, and it may not reflect the full picture of authority even within its training window if that authority was not well-represented in the training data.

This type is particularly relevant for rapidly developing areas of law: AI regulation, cryptocurrency, securities enforcement, environmental permitting, and immigration are all areas where the gap between model training and current practice is most likely to create a material error.

**The catch:** For any rapidly developing area of law, AI-generated research should be treated as a starting point for a primary-source search, not as a current-law summary. A Westlaw or Lexis search for recent authority on the point should be run regardless of what the AI returns.

## The Verification Protocol Maps to the Taxonomy

Each hallucination type has a corresponding catch that a well-designed workflow can systematize:

| Hallucination Type | Verification Step |
|---|---|
| Citation fabrication | Primary-source citation check (Westlaw or Lexis) |
| Attribution hallucination | Read the holding and locate quoted language verbatim |
| Statutory or regulatory fabrication | Pull and read the cited subsection |
| Jurisdictional or procedural hallucination | Jurisdiction-specific review for out-of-practice matters |
| Temporal hallucination | Current-authority search for developing areas of law |

A verification protocol that addresses only citation fabrication leaves four failure modes unaddressed. Firms that implemented citation checks after Mata v. Avianca and stopped there have a partial protocol, not a complete one.

The AI Legal Research case library documents instances of each type across court orders and sanctions proceedings. The pattern across those cases is consistent: the hallucination that caused the problem was not the type the attorney was watching for.

## Why the Taxonomy Matters for Professional Responsibility

The Model Rules do not distinguish between hallucination types. A false statement of law under Rule 3.3 is a false statement of law regardless of whether it arose from citation fabrication or attribution hallucination. But the supervision analysis under Rules 5.1 and 5.3 is different.

A partner reviewing a brief for citation accuracy is not necessarily reviewing it for attribution hallucination. A workflow that routes filings through a citation checker does not catch temporal hallucination. Supervisory procedures need to be designed against the full taxonomy, not just the type that generated the most press coverage.

The [framework in Ethics-Safe AI Use for Law Firms](/ai-ethics) maps each hallucination type to the specific supervisory checkpoint that addresses it and to the Model Rule provision that creates liability when that checkpoint is missing. Firms designing AI governance procedures benefit from treating the five types as distinct problems with distinct solutions, not as variations on a single theme.

---

The attorneys who have been sanctioned for AI-related filing errors were not careless practitioners. They were attorneys who understood one failure mode and did not know about the others. The taxonomy exists to close that gap.

*Christian Kameir is the author of [Ethics-Safe AI Use for Law Firms](/ai-ethics) documenting court orders and sanctions involving AI-generated legal content.*
