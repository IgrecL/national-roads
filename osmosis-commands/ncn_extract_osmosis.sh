osmosis \
  --read-pbf file="./Data/kansai-latest.osm.pbf" \
  --tf accept-relations network=ncn,rcn,icn \
  --used-way \
  --used-node \
  --write-xml file="./Data/ncn_rcn_icn_kansai.xml"


#--tf accept-ways network=ncn \