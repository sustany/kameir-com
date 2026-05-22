---
title: "AI Hallucinations in Legal Research: What Law Firms Must Know"
description: "AI tools are fabricating citations, statutes, and case holdings in legal filings. Here is what the documented cases show and what your firm needs to do before it happens to you."
publishedAt: 2026-05-22
draft: false
---

Courts have now sanctioned attorneys in multiple jurisdictions for submitting AI-generated briefs containing citations that do not exist. The cases are documented. The sanctions are real. And the attorneys in each instance said the same thing: they did not know the tool could fabricate authoritative-sounding text with complete confidence.

That is the problem. AI language models do not know what they do not know. And as I wrote recently on LinkedIn, [the AI ethics risk your law firm probably has not written down](https://www.linkedin.com/pulse/ai-ethics-risk-your-law-firm-probably-has-written-down-kameir-vu8cc/) is not the one showing up in the headlines. It is the undocumented assumption that the tool is doing what the attorney thinks it is doing. When a model has insufficient training data on a specific point of law, it does not return an error. It generates a plausible-sounding answer, complete with case names, docket numbers, and quotations, and presents it with the same tone it uses when the answer is accurate.

This piece covers what AI hallucinations are in a legal context, which Model Rules are implicated when things go wrong, what the documented cases show, and what a minimal verification protocol looks like in practice.

## What Makes Legal Research Uniquely Vulnerable

Hallucination is not a bug that will be patched in the next model release. It is a structural property of how large language models generate text. The model predicts the most statistically likely next token given its training data. In law, that means it has learned the patterns of how cases are cited, how holdings are summarized, and how statutes are formatted. It can reproduce those patterns for cases that do not exist.

Legal research is particularly exposed for three reasons.

**Specificity creates pressure to fabricate.** A litigator asking for cases supporting a narrow evidentiary argument in a specific circuit is asking for something the model may have limited data on. Rather than acknowledge that gap, the model fills it.

**Format provides false confidence.** A hallucinated citation looks exactly like a real one: proper reporter, volume, page number, year. There is no visual signal that distinguishes a fabricated cite from a legitimate one.

**Verification is non-trivial.** Checking every citation against Westlaw or Lexis takes time. Under deadline pressure, attorneys who trust the tool skip that step, and that is where sanctions begin.

## The Model Rules That Apply

Three rules create direct exposure when AI-generated content enters a filing without adequate verification.

**Rule 1.1 (Competence)** now includes technological competence. The ABA added Comment 8 in 2012 to require lawyers to keep abreast of changes in the law and its practice, including the benefits and risks of relevant technology. Using an AI tool without understanding its failure modes is a competence issue.

**Rule 3.3 (Candor Toward the Tribunal)** prohibits making false statements of law and requires disclosure when a lawyer has offered material evidence that is false. A hallucinated citation is a false statement of law. If an attorney discovers it after filing, Rule 3.3 requires corrective disclosure.

**Rule 5.1 and 5.3 (Supervision)** create liability up the chain. Partners and supervising attorneys are responsible for the work of associates and non-attorney staff. Delegating legal research to an AI tool without implementing reasonable oversight procedures is a supervision failure, not a technology failure.

The [framework in Ethics-Safe AI Use for Law Firms](/ai-ethics) maps each of these rules to specific workflows and identifies where firms are most likely to miss the checkpoint.

## What the Documented Cases Show

The [AI Legal Research case library](/AI-legal-research) tracks court orders, sanctions, and disciplinary proceedings involving AI-generated content. A few patterns emerge across those cases.

**The Mata v. Avianca pattern.** In the foundational 2023 case, attorneys submitted a brief containing citations to cases that did not exist. When opposing counsel could not locate the cases, the court ordered the attorneys to show cause. The attorneys initially represented that the cases were real. They were not. The court sanctioned the attorneys and referred the matter for disciplinary review. The issue was not that they used AI. It was that they submitted the AI output as their own work product without verification.

**Subsequent cases replicate the same structure.** An attorney uses an AI tool for initial research. The output includes plausible-sounding citations. The attorney does not run each citation through a primary source database. The filing goes out. Opposing counsel or the court cannot locate the cited authority. Sanctions follow. In several cases, the court ordered attorneys to disclose what AI tools were used and what verification steps were taken, establishing that courts now treat AI use as a discoverable workflow question.

**The holdings problem.** Beyond fabricated citations, courts have identified cases where the AI correctly identified a real case but mischaracterized the holding, sometimes reversing it. A case that held against the attorney's position was summarized as if it held in their favor. This is harder to catch than a phantom citation because the case exists; only the description is wrong.

## A Minimum Verification Protocol

A firm does not need a 40-page AI policy to manage this risk. It needs three things built into the workflow before any AI-assisted research enters a filing.

**1. Citation verification at primary sources.** Every case citation generated by an AI tool must be verified in Westlaw, Lexis, or an equivalent primary database before it is cited. This is not optional. The citation check should confirm: the case exists, the quoted language appears where the AI said it appears, and the holding has not been reversed or limited.

**2. Holding summary review.** For any case where the AI provides a summary of the holding, the reviewer should read at least the syllabus or headnotes in the primary source. A five-minute check against the original eliminates the holding-reversal problem.

**3. A supervision checkpoint before filing.** Any brief or motion that used AI assistance in its preparation should pass through a reviewer who did not do the original research. That reviewer's job is not to re-research the issue but to run the citation check independently. Fresh eyes catch what the original researcher normalizes.

These three steps add time. They add less time than responding to a sanctions motion.

## How to Evaluate an AI Tool Before Firm-Wide Deployment

Most law firms are evaluating or have already deployed AI tools without a formal assessment framework. The questions that matter are not in the marketing materials.

Ask the vendor: Does the tool retrieve from current primary source databases, or does it generate from training data? Retrieval-augmented generation systems that pull directly from Westlaw or Lexis have lower hallucination rates on citation tasks than pure generative systems. The distinction matters.

Ask your own team: What is the output of this tool being used for, and at what point does it enter a client-facing work product? Research assistance is different from drafting, which is different from citation-to-filing. Each step requires a different level of verification.

Run a controlled test before deployment. Give the tool a research question where you know the answer and know there is limited on-point authority. See what it returns. If it returns confident-sounding citations for a question that has no clear answer, that is diagnostic.

## FAQ

### Are courts requiring disclosure of AI use in filings?

Several federal districts and state courts have adopted local rules requiring disclosure when AI tools were used to draft a filing. The landscape is moving quickly. Check your local rules and standing orders before filing, and assume disclosure obligations will expand.

### Does using an AI tool that cites real cases eliminate hallucination risk?

No. Even tools connected to primary source databases can mischaracterize holdings, select inapposite cases, or generate analysis that does not follow from the cited authority. Citation accuracy and analytical accuracy are separate problems.

### What should a firm do if it discovers a hallucinated citation after filing?

Disclose to the tribunal immediately under Rule 3.3. Do not wait to see if opposing counsel catches it. Voluntary disclosure before the court identifies the problem is treated materially differently than disclosure after sanctions proceedings begin.

### Is AI-generated research covered by attorney-client privilege?

The research process itself is generally protected as attorney work product, but courts in sanctions proceedings have ordered disclosure of AI workflows as part of their authority to investigate the filing. The privilege question and the sanctions question are distinct.

### Does firm size change the risk profile?

Large firms have more internal review layers, which reduces the probability that an unverified AI output reaches a filing. But the Rule 5.1 and 5.3 supervision questions become more complex at scale, with more people using more tools with less uniform oversight. The risk is distributed differently, not eliminated.

---

The bar is catching up faster than most firms expected. Courts are not waiting for professional responsibility bodies to act. They are using their inherent sanctioning authority now. The attorneys facing those sanctions are not outliers. They are practitioners who adopted a widely marketed tool, trusted its output, and skipped the verification step that would have caught the problem.

The verification protocol is not complicated. Building it into the workflow before the first sanctionable filing is the point of the exercise.

*Christian Kameir advises law firms and legal technology companies on AI governance and ethics. His book [Ethics-Safe AI Use for Law Firms](/ai-ethics) covers the Model Rules framework, hallucination taxonomy, and firm-level implementation in detail. The [AI Legal Research case library](/AI-legal-research) tracks documented court orders and sanctions involving AI-generated legal content.*