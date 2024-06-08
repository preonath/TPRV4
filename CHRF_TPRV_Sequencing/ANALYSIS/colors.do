* Year (CHRF only)
gen year_color="#feedde" if year==2017
replace year_color="#fdd0a2" if year==2018
replace year_color="#fdae6b" if year==2019
replace year_color="#fd8d3c" if year==2020
replace year_color="#e6550d" if year==2021
replace year_color="#a63603" if year==2022

* Year (CHRF & NCBI)
gen year_color="#034e7b" if year==1980
replace year_color="#0570b0" if year==2002
replace year_color="#3690c0" if year==2005
replace year_color="#74a9cf" if year==2006
replace year_color="#a6bddb" if year==2007
replace year_color="#d0d1e6" if year==2012
replace year_color="#f1eef6" if year==2015
replace year_color="#feedde" if year==2017
replace year_color="#fdd0a2" if year==2018
replace year_color="#fdae6b" if year==2019
replace year_color="#fd8d3c" if year==2020
replace year_color="#e6550d" if year==2021
replace year_color="#a63603" if year==2022

* TLC
gen tlcgr_color="#ffffd9" if TLCGroup=="1-9"
replace tlcgr_color="#edf8b1" if TLCGroup=="10-49"
replace tlcgr_color="#c7e9b4" if TLCGroup=="150-199"
replace tlcgr_color="#7fcdbb" if TLCGroup=="250-299"
replace tlcgr_color="#41b6c4" if TLCGroup=="300-349"
replace tlcgr_color="#1d91c0" if TLCGroup=="350-399"
replace tlcgr_color="#225ea8" if TLCGroup=="50-99"
replace tlcgr_color="#0c2c84" if TLCGroup==">=500"

* Outcome
gen outcome_color="#3182bd" if Outcome=="DORB"
replace outcome_color="#fb6a4a" if Outcome=="Died"
replace outcome_color="#66c2a4" if Outcome=="Discharged"

* Co-infection Organism
gen orga_color="#8dd3c7" if organism == "Acinetobacter baumanii"
replace orga_color="#ffffb3" if organism == "Acinetobacter sp."
replace orga_color="#bebada" if organism == "Escherichia coli"
replace orga_color="#fb8072" if organism == "K. pneumoniae"
replace orga_color="#80b1d3" if organism == "Pseudomonas spp."
replace orga_color="#fdb462" if organism == "S. pneumoniae"
replace orga_color="#f0f0f0" if organism == ""


* Country
gen Country_color="#4daf4a" if Country=="Bangladesh"
replace Country_color="#e41a1c" if Country=="China"
replace Country_color="#377eb8" if Country=="Coted'Ivoire"
replace Country_color="#984ea3" if Country=="Germany"
replace Country_color="#ff7f00" if Country=="Ghana"
replace Country_color="#ffff33" if Country=="India"
replace Country_color="#a65628" if Country=="SouthAfrica"
replace Country_color="#f781bf" if Country=="USA"

* genotype
gen geno_color="#efedf5" if genotype==1
replace geno_color="#bcbddc" if genotype==2
replace geno_color="#756bb1" if genotype==3
