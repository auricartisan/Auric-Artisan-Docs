---
title: Chromatic Adaptation — Compare transforms and copy a matrix
description: Read the adaptation matrix, check its round trip, copy it as code, and compare all eight transforms on your illuminant pair.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Compare transforms and copy a matrix

## The maths in one line

Every transform in the lab has the same shape:

```text
X′ = M⁻¹ · diag(d) · M · X
d = 1 + D × (ρ_destination ÷ ρ_source − 1)   for each of L, M, S
```

M converts XYZ into a cone-like space. diag(d) scales each cone channel by the ratio of the destination white to the source white, softened by the degree of adaptation D. M⁻¹ converts back. The transforms differ only in M.

## The eight transforms

| Transform | Source of the matrix | Notes |
| --- | --- | --- |
| Bradford | Lam 1985 | The usual choice in ICC colour management; the reference the comparison is measured against |
| Von Kries | Hunt–Pointer–Estévez (Estévez 1979), normalised to D65 | Reads the same as HPE, because normalising rows cancels out in the formula |
| CAT02 | CIE 159:2004 (CIECAM02) | — |
| CAT16 | Li et al. 2017 (CAM16) | — |
| Sharp | Finlayson and Süsstrunk 2000 | A spectrally sharpened matrix |
| CMCCAT2000 | Li, Luo, Rigg and Hunt 2002 | — |
| HPE | Hunt–Pointer–Estévez | — |
| XYZ scaling | Identity matrix | The null case: scales X, Y and Z directly |

## Read and copy the matrix

1. Choose the illuminants and transform on the **Lab** tab, and set **Degree of adaptation D**.
2. Open the **Matrix** tab. The title names the transform, the pair and the D, for example "Bradford, D65 → D50 at D = 1.00".
3. Read the three blocks:
   - **M — XYZ to cone-like**: the transform's own matrix;
   - **diag(d)**: the three cone gains, with the formula beneath;
   - **Full adaptation matrix**: the single 3 × 3 matrix that takes XYZ under the source white to XYZ under the destination white.
4. Under **Decimals**, choose **4**, **6** (default) or **9**. Published matrices carry four to six figures; nine shows the round-off residue, which is useful when checking an inverse.
5. Check **Round trip**: the largest error of M⁻¹ × M against the identity matrix, recomputed every time.
6. Under **Copy as**, choose **NumPy**, **JSON**, **CSS matrix3d** or **GLSL mat3**. The transform's M matrix is copied to your clipboard in that form.

What each format contains:

| Format | Content |
| --- | --- |
| NumPy | `import numpy as np` and `M = np.array([...])` with the three rows |
| JSON | An object with the transform name, its citation and M as three rows |
| CSS matrix3d | A `matrix3d(...)` value with M in the upper-left 3 × 3 and the rest of a 4 × 4 identity |
| GLSL mat3 | `const mat3 M = mat3(...)` in column-major order, as GLSL expects |

The copy buttons copy M, not the full adaptation matrix. The full matrix for the current moment is in the JSON export on the **Export** tab.

## Compare all eight on your pair

The **All eight on this pair** list on the Matrix tab shows what each transform does, not which is more accurate. For each transform:

| Column | Meaning |
| --- | --- |
| Transform | The name; the one selected in the Lab is highlighted |
| ΔE vs Bradford | Mean CIEDE2000 difference between this transform's result and Bradford's over a fixed 12-colour probe |
| cond(M) | The matrix's condition number: how much it can stretch a difference. A description, not a quality score |
| Source | The paper the matrix comes from |
| Status | **Published**, or **Null case** for XYZ scaling |

Rows are sorted by ΔE vs Bradford, smallest first. Ranking transforms by accuracy would need the published corresponding-colour data sets, which the lab does not hold (see the Data tab).

## The Compare All Methods panel

On the **Export** tab, **Compare All Methods** runs all eight transforms at the current moment of the Lab timeline over eight test colours (#735244, #C29682, #627A9D, #D3AF37, #FF6347, #3BB273, #FFFFFF and #000000). For each it reports the **Mean ΔE₀₀**, **Median**, **Min** and **Max** colour shift between the colour under the source white and the adapted colour under the destination white, plus **det(M)** and **‖M‖F** of the full adaptation matrix. A bar chart shows the means, and a star marks the transform with the smallest mean shift. That is the smallest change on these eight colours, not proof of the most accurate transform.

## Result

You have the exact matrix for your adaptation, verified by its round trip, in the code format you need, and a picture of how the eight transforms differ on your pair.
