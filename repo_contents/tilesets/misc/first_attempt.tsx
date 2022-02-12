<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.5" tiledversion="1.7.2" name="first_attempt" tilewidth="32" tileheight="32" spacing="1" margin="1" tilecount="100" columns="10">
 <image source="first_attempt.png" width="331" height="331"/>
 <wangsets>
  <wangset name="Grasses" type="mixed" tile="21">
   <wangcolor name="Grass 1" color="#005500" tile="21" probability="1"/>
   <wangcolor name="Grass 2" color="#00aa00" tile="22" probability="1"/>
   <wangcolor name="Grass 3" color="#55aa00" tile="31" probability="1"/>
   <wangtile tileid="21" wangid="3,3,3,3,3,3,3,3"/>
   <wangtile tileid="22" wangid="2,2,2,2,2,2,2,2"/>
   <wangtile tileid="31" wangid="3,3,3,3,3,3,3,3"/>
  </wangset>
  <wangset name="Patchy Dirt" type="mixed" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="1" wangid="1,1,1,1,1,1,1,1"/>
   <wangtile tileid="2" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="3" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="4" wangid="0,1,0,1,0,1,0,1"/>
  </wangset>
 </wangsets>
</tileset>
