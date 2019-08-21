# Training Tiny Turtles

Learning [GraphDB](https://www.ontotext.com/products/graphdb/) with a reduced dataset

# A0 turtles

Swine Surveillance strains have an A0 barcode. Ergo initially many of the turtles will be A0-specific.

## A0\_genbank.ttl

This turtle will pull out metadata from the A0 strain genbanks.

* genbank
	* p:type "genbank"
	* p:genbank genbank 
	* p:strain strain
	* p:country country
	* p:state state
	* p:nucl nucl\_checksum
	* p:protid prot\_checksum
	* p:ao A0\_barcode
	* p:host swine
	* p:year
	* p:month
	* p:day
	* p:coldate

* strain
	* p:type "strain"
	* p:ha | p:na | .... genbankid

## A0\_clade.ttl

The swine surveillance strain segments (A0 barcode) will be classified based on nucleotide fasta sequence.

* genbank
	* p:segment_name
	* p:segment_num
	* p:clade 
	* p:htype (optional)
	* p:ntype (optional)

## A0\_motif\_h3.ttl

Looking at region 145, 155, 156, 158, 159, 189, and 193.

* genbank
	* p:pos145
	* p:pos155
	* p:pos156
	* p:pos158
	* p:pos159
	* p:pos189
	* p:pos193
	* p:h3motif (altho this can be inferred...)

## A0\_motif\_h1.ttl

Looking at region Sa, Sb, Ca1, Ca2, Cb regions. Maybe separate this out?

* genbank
	* p:Sa
	* p:Sb
	* p:Ca1
	* p:Ca2
	* p:Cb

## gisaid.ttl

* epiid
	* p:epi\_isolate
	* p:segment\_name
	* p:segment\_num
	* p:clade

## Reference.ttl

* genbank
	* p:tag "REF"

## EXP111.ttl

* EXP
	* p:pignum
	* p:strain
	* p:hi\_titor

	
---

# A Reduced Dataset

* Pick a few from each clade and segment
	* Earliest, latest, WGS, and partial
* Pick a few non-A0 swine
* Pick a few human
* Pick a few mixed
* Pick a few conflicting date strains
* Pick a few outside USA strains
* a few EPI strains



