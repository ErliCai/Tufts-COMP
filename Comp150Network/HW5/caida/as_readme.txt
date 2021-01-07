http://www.caida.org/data/as-taxonomy/

Publication
Revealing the Autonomous System Taxonomy: The Machine Learning Approach (pdf) 
Xenofontas Dimitropoulos, Dmitri Krioukov, George Riley, KC Claffy 
Passive and Active Measurements Workshop (PAM), Mar. 2006.

AS taxonomy and attributes
The file as2attr.tgz includes the set of AS attributes we extracted from CAIDA, RouteViews, and Internet Routing Registries data. Each line contains the following tab delimited fields: 1) AS number, 2) organization description record, 3) number of inferred providers, 4) number of inferred peers, 5) number of inferred customers, 6) equivalent number of /24 prefixes covering all the advertised IP space, 7) number of advertised IP prefixes, and 8) inferred AS class. The classes are encoded with the following acronyms: "t1" for large ISPs, "t2" for small ISPs, "edu" for Universities, "ix" for IXPs, "nic" for NICs, "comp" for Customers and "abstained" for ASes for which the algorithm did not make a prediction.

AS relationships
The file as_rel.tgz includes the AS graph annotated with inferred AS relationships. Our inference is based on heuristics we developed in our previous work. In particular, customer-to-provider relationships are inferred using the methodology of the paper Inferring AS Relationships: Dead End or Lively Beginning?, while peer-to-peer links are inferred using the methodology of the paper "AS Relationships: Inferance and Validation", which is currently under submission (we hope to post a link here soon). Each line in as_rel.txt is a triplet: A B C, where A B reflects an AS link and C the AS relationship: if (C==0) A B is a p2p link; if (C=-1) A is a customer of B; and if (C==1) A is a provider of B. Each AS link is listed twice as A B and B A. Note that few of the AS numbers listed in as_rel.txt are missing from as2attr.txt, since in the latter we include only the AS numbers for which all six attributes were available.
