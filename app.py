import streamlit as st
from upgraded_truthos import TruthOS_Upgraded
import json

st.set_page_config(page_title="TruthOS", layout="centered")
st.title("🧠 TruthOS Symbolic Claim Verifier")
st.markdown("Enter a symbolic or factual claim below. TruthOS will score it based on recursion, entropy, ambiguity, contradiction, and symbolic consistency.")

truth = TruthOS_Upgraded()
claim = st.text_area("Your Claim", height=120, placeholder="e.g. Freedom is slavery.")

if st.button("Verify"):
    if not claim.strip():
        st.warning("Please enter a claim before verifying.")
    else:
        verdict = truth.verify(claim)
        st.markdown(f"### 🧾 Verdict: `{verdict}`")

        with st.expander("📜 Internal Log"):
            for entry in truth.log:
                st.text(entry)

        with st.expander("🔣 Verdict Legend"):
            st.markdown("""
            - `T` = High confidence truth
            - `Δ` = Likely truth, not fully confirmed
            - `◬` = Ideological contradiction detected
            - `?` = Ambiguous or unclear
            - `⊗` = Low coherence or symbolic inconsistency
            - `⊘` = Hard falsehood or logical contradiction
            """)

        st.download_button(
            "📥 Download Full Log",
            data=json.dumps({"claim": claim, "verdict": verdict, "log": truth.log}, indent=2),
            file_name="truthos_verdict.json",
            mime="application/json"
        )

st.markdown("---")
st.caption("TruthOS Upgraded • Balanced Scoring Patch")
