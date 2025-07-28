import spacy
from spacy.cli import download
import re
import math
import hashlib
import numpy as np
from numpy.fft import fft

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

class TruthOS_Upgraded:
    def __init__(self):
        self.log = []

    def verify(self, operation):
        self.log = []
        self.log.append(f"Verifying Claim: {operation}")

        if self.hard_truth_check(operation):
            self.log.append("🚫 Immutable Violation")
            return self.halt("Hard contradiction")

        soft_flags = self.soft_contradiction_check(operation)
        contradiction = self.semantic_contradiction_check(operation)

        segmented_units = self.symbolic_shor(operation)
        named_entities = self.named_entity_recognition(operation)
        fft_values = self.fft_analysis(operation)
        entropy = self.signal_entropy(operation)
        ambiguity_flags = self.detect_symbolic_ambiguity(operation)
        containment_flags = self.detect_containment_language(operation)
        recursion_score = self.recursive_consistency_check(segmented_units)

        penalty = len(ambiguity_flags) * 0.15 + len(containment_flags) * 0.2
        base_score = self.truth_weight(fft_values, entropy, recursion_score, segmented_units)
        truth_score = max(0.0, round(base_score - penalty, 2))

        self.log.append(f"⬟ Prime Narrative Units: {segmented_units}")
        self.log.append(f"⬠ Named Entities: {named_entities}")
        self.log.append(f"φ FFT Harmonics: {fft_values[:5]}")
        self.log.append(f"Entropy: {entropy:.3f}")
        self.log.append(f"Recursion Score: {recursion_score}/10")
        self.log.append(f"Truth Score: {truth_score}/10")

        if ambiguity_flags:
            self.log.append(f"⚠️ Ambiguity Detected: {ambiguity_flags}")
        if containment_flags:
            self.log.append(f"⚠️ Containment Detected: {containment_flags}")
        if soft_flags:
            self.log.append(f"⚠️ Ideological Contradiction Detected: {soft_flags}")

        # Revised verdict logic
        if contradiction:
            verdict = "⊘"
        elif truth_score >= 8.5 and not ambiguity_flags and recursion_score >= 7.0:
            verdict = "T"
        elif soft_flags:
            verdict = "◬"
        elif truth_score >= 6.5:
            verdict = "Δ"
        elif truth_score >= 4.5:
            verdict = "?"
        elif truth_score > 2.5:
            verdict = "⊗"
        else:
            verdict = "⊘"

        self.log.append(f"∂τs = 0 — Final Truth State: {verdict}")
        anchor = hashlib.sha256(operation.encode()).hexdigest()
        self.log.append(f"⬟ Anchor Hash: {anchor}")
        return verdict

    def hard_truth_check(self, text):
        patterns = [r"2\s*\+\s*2\s*=\s*5", r"1\s*=\s*0", r"earth is flat", r"triangles have four sides"]
        return any(re.search(p, text, re.I) for p in patterns)

    def soft_contradiction_check(self, text):
        flags = [r"freedom is slavery", r"truth is relative", r"ignorance is strength"]
        return [f for f in flags if re.search(f, text, re.I)]

    def semantic_contradiction_check(self, text):
        patterns = [r"mutually exclusive", r"both true and false"]
        return any(re.search(p, text, re.I) for p in patterns)

    def symbolic_shor(self, text):
        return [t.strip() for t in text.split('.') if 0 < len(t.strip().split()) <= 8]

    def named_entity_recognition(self, text):
        return [ent.text for ent in nlp(text).ents]

    def fft_analysis(self, text, window=64):
        arr = np.array([ord(c) for c in text])
        if len(arr) < window:
            arr = np.pad(arr, (0, window - len(arr)))
        fft_vals = np.abs(fft(arr[:window]))
        return [round(v, 2) for v in fft_vals[:10]]

    def signal_entropy(self, text):
        p = [text.count(c) / len(text) for c in set(text)]
        return -sum(pi * math.log2(pi) for pi in p if pi > 0)

    def detect_symbolic_ambiguity(self, text):
        patterns = [r"illusion", r"metaphor", r"not literally"]
        return [p for p in patterns if re.search(p, text, re.I)]

    def detect_containment_language(self, text):
        patterns = [r"debunked", r"conspiracy", r"experts agree"]
        return [p for p in patterns if re.search(p, text, re.I)]

    def recursive_consistency_check(self, units):
        matches = 0
        for u in units:
            for other in units:
                if u != other and (u in other or other in u):
                    matches += 1
        return min(round((matches / max(1, len(units))) * 10, 2), 10)

    def truth_weight(self, fft_vals, entropy, recursion_score, units):
        h = min(sum(fft_vals[:3]) / 300, 1.0)
        e = min(entropy / 8, 1.0)
        r = min(recursion_score / 12, 1.0)
        u = min(len(units) / 10.0, 1.0)
        return round((h + e + r + u) / 4 * 10, 2)

    def halt(self, reason):
        self.log.append(f"⛔ HALTED: {reason}")
        return "⊘"
