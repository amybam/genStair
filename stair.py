import rhinoscriptsyntax as rs
import Rhino


if not rs.CurveDirectionsMatch(A, B):
    rs.ReverseCurve(A)

srf = rs.AddEdgeSrf((A,B))
ptA = rs.CurveMidPoint(A)
ptB = rs.CurveMidPoint(B)

if ptA[2]>ptB[2]:
    pt=ptA
else:
    pt=ptB


dom = rs.SurfaceDomain(srf,1)
param= rs.SurfaceNormalizedParameter(srf,dom)
axs = rs.ExtractIsoCurve(srf, param, 0)
