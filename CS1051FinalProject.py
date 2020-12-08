import random
gearCompared = False

sim_asker = str(input("Would you like to sim your gear? Y)Yes N)No"))
if sim_asker == "Y":
    simCollector = True
else:
    simCollector = False

'''For values (int,haste,crit,vers,mastery)'''
Helm = {"H1" : [80,80,0,80,0], "H" : [40,40,0,40,0], "Shadowscale Helm" : [40,40,0,40,0], "test_helm" : [50,150,0,105,0], "Nathrian Usurper's Mask HD" : [49,36,0,66,0],"Nathrian Usurper's Mask MD" : [55,39,0,73,0], "Soulthorn Visage HD" : [49,36,0,0,66],  "Soulthorn Visage MD" : [55,39,0,0,73], "Rattling Deadeye Hood HD" : [49,0,66,0,36], "Rattling Deadeye Hood MD" : [55,0,73,0,39], "Ampitheater Stalker's Hood HD" : [49,59,0,0,42], "Ampitheater Stalker's Hood MD" : [55,65,0,0,45], "Helm of Insatiable Appetite LFR" : [56,78,0,0,34],  "Helm of Insatiable Appetite N" : [64,85,0,0,37],  "Helm of Insatiable Appetite H" : [72,92,0,0,40],  "Helm of Insatiable Appetite M" : [82,99,0,0,43]}


Neck = {"N1" : [0,120,0,48,0], "N" : [0,60,0,24,0], "Reconstructed Family Locket" : [0,60,0,24,0], "test_neck" : [50,0,150,0,105], "Sin Stained Pendant HD" : [0,90,0,0,36], "Sin Stained Pendant MD" : [0,105,0,0,42], "Trailspinner Pendant HD" : [0,0,47,0,78], "Trailspinner Pendant MD" : [0,0,54,0,93], "Azure-Venom Choker HD" : [0,0,84,41,0], "Azure-Venom Choker MD" : [0,0,98,48,0], "Muckformed Chain Choker" : [0,0,79,105,0], "Charm of Eternal Winter LFR" : [0,38,0,0,112], "Charm of Eternal Winter N" : [0,44,0,0,127],  "Charm of Eternal Winter H" : [0,50,0,0,144],  "Charm of Eternal Winter M" : [0,55,0,0,159], "Noble's Birthstone Pendant LFR" : [0,0,37,0,115], "Noble's Birthstone Pendant N" : [0,0,42,0,130], "Noble's Birthstone Pendant H" : [0,0,47,0,147], "Noble's Birthstone Pendant M" : [0,0,52,0,162]}


Shoulder = {"S1" : [62,58,58,0,0], "S" : [31,29,29,0,0], "Shadowscale Pauldrons" : [31,29,29,0,0], "test_shoulders" : [60,0,105,120,0], "Mantle of Ephemeral Visages MD" : [41,0,0,30,51], "Mantle of Ephemeral Visages HD" : [36,0,0,28,47], "Wintersnap Shoulderguards HD" : [36,47,0,0,28], "Wintersnap Shoulderguards MD" : [41,51,0,0,30], "Plagueborne Shoulderguards HD" : [36,0,44,31,0],  "Plagueborne Shoulderguards MD" : [41,0,48,35,0], "Blightbone Spaulders HD" : [36,0,0,47,28], "Blightbone Spaulders MD" : [41,0,0,51,30], "Pauldrons of Fatal Finality LFR" : [45,0,0,26,62], "Pauldrons of Fatal Finality N" : [51,0,0,29,66], "Pauldrons of Fatal Finality H" : [58,0,0,32,71], "Pauldrons of Fatal Finality M" : [65,0,0,34,76]}


Back = {"B1" : [40,0,0,30,34], "B" : [20,0,0,15,17], "Dredwing Shroud" : [20,0,0,15,17], "test_back" : [35,120,0,0,150], "Dealer Xy'exa's Cape HD" : [27,0,0,22,34], "Dealer Xy'exa's Cape MD" : [31,0,0,24,38], "Blighted Margrave's Cloak HD" : [27,20,0,36,0], "Blighted Margrave's Cloak MD" : [31,22,0,41,0], "Cloak of Enveloping Manifestations HD" : [27,0,34,0,22],  "Cloak of Enveloping Manifestations MD" : [31,0,38,0,24], "Drape of Twisted Loyalties HD" : [27,36,20,0,0], "Drape of Twisted Loyalties MD" : [31,41,22,0,0], "Shroud of the Penitent" : [38,25,46,0,0], "Cowled Batwing Cloak LFR" : [32,0,0,42,21], "Cowled Batwing Cloak N" : [36,0,0,46,23], "Cowled Batwing Cloak H" : [40,0,0,49,24], "Cowled Batwing Cloak M" : [46,0,0,53,26], "Mantle of Manifest Sins LFR" : [32,0,43,0,21],  "Mantle of Manifest Sins N" : [36,0,46,0,21],  "Mantle of Manifest Sins H" : [40,0,51,0,23],  "Mantle of Manifest Sins M" : [46,0,53,0,26], "Crest of the Legionnaire General LFR" : [34,45,0,20,0],  "Crest of the Legionnaire General N" : [38,49,0,22,0],  "Crest of the Legionnaire General H" : [43,52,0,24,0],  "Crest of the Legionnaire General M" : [49,57,0,25,0]}


Chest = {"C1" : [80,0,80,0,80], "C" : [40,0,40,0,40], "Shadowscale Vest" : [40,0,40,0,40], "test_chest" : [60,150,0,0,90], "Harness of Twisted Whims HD" : [49,59,42,0,0], "Harness of Twisted Whims MD" : [55,65,45,0,0], "Soaring Decimator's Hauberk HD" : [49,0,40,0,63], "Soaring Decimator's Hauberk MD" : [55,0,44,0,68], "Forsworn Stalker's Hauberk HD" : [49,0,42,59,0], "Forsworn Stalker's Hauberk MD" : [55,0,45,65,0], "Triumphant Combatant's Chainmail HD" : [49,36,66,0,0], "Triumphant Combatant's Chainmail MD" : [55,39,73,0,0], "Mortanis's Ribcage" : [68,0,0,45,83], "Master Huntsman's Bandolier LFR" : [56,0,39,0,74], "Master Huntsman's Bandolier N" : [64,0,42,0,79], "Master Huntsman's Bandolier H" : [72,0,45,0,86], "Master Huntsman's Bandolier M" : [82,0,49,0,93], "Consumptive Chainmail Carapace LFR" : [56,39,0,74,0], "Consumptive Chainmail Carapace N" : [64,42,0,79,0], "Consumptive Chainmail Carapace H" : [72,45,0,86,0], "Consumptive Chainmail Carapace M" : [82,49,0,93,0]}


Wrist = {"W1" : [46,44,44,0,0], "W" : [23,22,22,0,0], "Shadowscale Armguards" : [23,22,22,0,0], "test_wrist" : [35,150,0,90,0], "Hivesawrm Bracers HD" : [27,0,0,23,33], "Hivesawrm Bracers MD" : [31,0,0,25,36], "Tortured Assistant's Bindings HD" : [27,0,0,37,20], "Tortured Assistant's Bindings MD" : [31,0,0,41,21], "Shackles of Alluring Vitality HD" : [27,0,34,22,0],  "Shackles of Alluring Vitality MD" : [31,0,38,24,0], "Fallen Paragon's Armguards HD" : [27,37,0,20,0], "Fallen Paragon's Armguards MD" : [31,41,0,21,0], "Ironroot Bindings" : [38,26,0,45,0], "Bangles of Errant Pride LFR" : [32,0,42,0,21],  "Mantle of Manifest Sins N" : [36,0,44,0,23],  "Mantle of Manifest Sins H" : [40,0,48,0,24],  "Mantle of Manifest Sins M" : [46,0,52,0,27]}


Hands = {"Ha1" : [62,0,58,0,58], "Ha" : [31,0,29,0,29], "Shadowscale Gauntlets" : [31,0,29,0,29], "test_hands" : [55,0,150,0,150], "Hakkari Revenant's Grips HD" : [36,47,28,0,0], "Hakkari Revanant's Grips MD" : [41,51,31,0,0], "Iron Spiked Handgrips HD" : [36,0,31,0,44], "Iron Spiked Handgrips MD" : [41,0,35,0,48], "Absonant Construct's Handguards HD" : [36,28,0,47,0], "Absonant Construct's Handguards MD" : [41,30,0,51,0], "Grips of Overwhelming Beatings HD" : [36,29,45,0,0],  "Grips of Overwhelming Beatings MD" : [41,32,50,0,0], "Bone Crushing Vicegrips" : [51,60,35,0,0], "Castellan's Chainlink Grips LFR" : [43,0,61,0,24], "Castellan's Chainlink Grips N" : [48,0,66,0,26], "Castellan's Chainlink Grips H" : [54,0,71,0,28], "Castellan's Chainlink Grips M" : [61,0,75,0,30], "Oathsworn Soldier's Gauntlets LFR" : [45,31,57,0,0],  "Oathsworn Soldier's Gauntlets N" : [51,33,62,0,0],  "Oathsworn Soldier's Gauntlets H" : [58,36,67,0,0],  "Oathsworn Soldier's Gauntlets M" : [65,38,71,0,0]}



Waist = {"Wst1" : [62,58,58,0,0], "Wst" : [31,29,29,0,0], "Shadowscale Waistguard" : [31,29,29,0,0], "test_waist" : [45,0,0,150,90], "Clasp of Waning Shadow HD" : [36,0,0,45,29], "Clasp of Waning Shadow MD" : [41,0,0,50,32], "Belt of Wretched Manipulations HD" : [36,0,47,28,0], "Belt of Wretched Manipulations MD" : [41,0,51,30,0], "Executor's Prideful Girdle HD" : [36,48,0,26,0], "Executor's Prideful Girdle MD" : [41,53,0,28,0], "Dark Praetorian's Clasp HD" : [36,0,0,29,45], "Dark Praetorian's Clasp MD" : [41,0,0,32,50], "Servo-Chain Waistguard" : [51,39,56,0,0], "Double-Chained Utility Belt LFR" : [43,0,0,55,28], "Double-Chained Utility Belt N" : [48,0,0,60,31], "Double-Chained Utility Belt H" : [54,0,0,66,33], "Double-Chained Utility Belt M" : [61,0,0,70,36], "Load-Bearing Belt LFR" : [43,58,0,25,0],  "Load-Bearing Belt N" : [48,63,0,27,0],  "Load-Bearing Belt H" : [54,69,0,30,0],  "Load-Bearing Belt M" : [61,74,0,32,0]}


Legs = {"L1" : [80,0,80,80,0], "L" : [40,0,40,40,0], "Shadowscale Greaves" : [40,0,40,40,0], "test_legs" : [55,180,165,0,0], "Techno-Coil Leggaurds HD" : [49,36,0,0,66], "Techno-Coil Leggaurds MD" : [55,39,0,0,73], "Blightborne Chain Legguards HD" : [49,0,63,0,40], "Blightborne Chain Legguards MD" : [55,0,68,0,44], "Wind Dancer's Legguards HD" : [49,64,0,0,37], "Wind Dancer's Legguards MD" : [55,70,0,0,41], "Lichbone Legguards HD" : [49,40,0,63,0], "Lichbone Legguards MD" : [55,44,0,68,0], "Greaves of Enigmatic Energies LFR" : [56,0,77,0,36],  "Greaves of Enigmatic Energies N" : [64,0,84,0,39],  "Greaves of Enigmatic Energies H" : [72,0,91,0,41],  "Greaves of Enigmatic Energies M" : [82,0,96,0,44], "Memento-Laden Cuisses LFR" : [56,74,0,37,0], "Memento-Laden Cuisses N" : [64,81,0,42,0], "Memento-Laden Cuisses H" : [72,86,0,45,0], "Memento-Laden Cuisses M" : [82,94,0,48,0]}


Feet = {"F" : [31,29,0,29,0], "Shadowscale Treads" : [31,29,0,29,0], "test_feet" : [45,135,0,0,135], "Spatial Rift Striders HD" : [36,45,29,0,0], "Spatial Rift Striders MD" : [41,50,32,0,0], "Shardskin Sabatons HD" : [36,0,31,0,44], "Shardskin Sabatons MD" : [41,0,35,0,48], "Striders of Restless Malice HD" : [36,0,31,44,0], "Striders of Restless Malice MD" : [41,0,35,48,0], "Boots of Shuddering Matter HD" : [36,28,47,0,0], "Boots of Shuddering Matter MD" : [41,30,51,0,0], "Jingling Stone Stompers" : [51,38,0,57,0], "Stoneclas Stompers LFR" : [43,0,60,0,25],  "Stoneclas Stompers N" : [48,0,65,0,27], "Stoneclas Stompers H" : [54,0,69,0,30], "Stoneclas Stompers M" : [61,0,74,0,31]}


Finger1 = {"F1" : [0,40,0,0,51], "Gargon Eye Ring" : [0,40,0,0,51], "test_finger1" : [45,0,0,0,0], "Death God's Signet HD" : [0,90,0,0,36], "Death God's Signet MD" : [0,105,0,0,42], "Signet of the False Accuser HD" : [0,37,0,0,88],  "Signet of the False Accuser MD" : [0,44,0,0,103], "Arachnid Cipher Ring HD" : [0,49,76,0,0],  "Arachnid Cipher Ring MD" : [0,58,88,0,0], "Entwined Gorger Tendril HD" : [0,0,73,52,0],  "Entwined Gorger Tendril MD" : [0,0,85,61,0], "Sitchflesh's Misplaced Signet HD" : [0,81,0,45,0],  "Sitchflesh's Misplaced Signet MD" : [0,94,0,52,0], "Ritual Commander's Ring HD" : [0,0,48,77,0], "Ritual Commander's Ring MD" : [0,0,57,90,0], "Bloodoath Signet HD" : [0,73,52,0,0], "Bloodoath Signet MD" : [0,85,61,0,0], "Fleshfused Circle HD" : [0,0,37,0,88],  "Fleshfused Circle MD" : [0,0,44,0,103], "Ritual Bone Band HD" : [0,0,0,85,40], "Ritual Bone Band MD" : [0,0,0,101,45], "Ring of Perpetual Conflict HD" : [0,0,83,0,42], "Ring of Perpetual Conflict MD" : [0,0,97,0,50], "Band of the Risen Bonelord" : [0,83,0,0,99], "Twisted Witherroot Band" : [0,0,95,89,0], "Hyperlight Band LFR" : [0,0,0,110,41], "Hyperlight Band N" : [0,0,0,126,46], "Hyperlight Band H" : [0,0,0,141,53], "Hyperlight Band M" : [0,0,0,157,58], "Ritualist's Treasured Ring LFR" : [0,116,34,0,0], "Ritualist's Treasured Ring N" : [0,133,39,0,0],"Ritualist's Treasured Ring H" : [0,149,44,0,0], "Ritualist's Treasured Ring M" : [0,165,49,0,0], "Most Regal Signet of Sire Denathrius LFR" : [0,128,0,0,34], "Most Regal Signet of Sire Denathrius N" : [0,144,0,0,39], "Most Regal Signet of Sire Denathrius H" : [0,161,0,0,44], "Most Regal Signet of Sire Denathrius M" : [0,178,0,0,48]}


Finger2 = {"F2" : [0,46,46,0,0], "Night Courtier's Ring" : [0,46,46,0,0], "test_finger2" : [0,135,0,0,0], "Death God's Signet HD" : [0,90,0,0,36], "Death God's Signet MD" : [0,105,0,0,42], "Signet of the False Accuser HD" : [0,37,0,0,88],  "Signet of the False Accuser MD" : [0,44,0,0,103], "Arachnid Cipher Ring HD" : [0,49,76,0,0],  "Arachnid Cipher Ring MD" : [0,58,88,0,0], "Entwined Gorger Tendril HD" : [0,0,73,52,0],  "Entwined Gorger Tendril MD" : [0,0,85,61,0], "Sitchflesh's Misplaced Signet HD" : [0,81,0,45,0],  "Sitchflesh's Misplaced Signet MD" : [0,94,0,52,0],  "Ritual Commander's Ring HD" : [0,0,48,77,0], "Ritual Commander's Ring MD" : [0,0,57,90,0], "Bloodoath Signet HD" : [0,73,52,0,0], "Bloodoath Signet MD" : [0,85,61,0,0], "Fleshfused Circle HD" : [0,0,37,0,88],  "Fleshfused Circle MD" : [0,0,44,0,103], "Ritual Bone Band HD" : [0,0,0,85,40], "Ritual Bone Band MD" : [0,0,0,101,45], "Ring of Perpetual Conflict HD" : [0,0,83,0,42], "Ring of Perpetual Conflict MD" : [0,0,97,0,50], "Band of the Risen Bonelord" : [0,83,0,0,99], "Twisted Witherroot Band" : [0,0,95,89,0], "Hyperlight Band LFR" : [0,0,0,110,41], "Hyperlight Band N" : [0,0,0,126,46], "Hyperlight Band H" : [0,0,0,141,53], "Hyperlight Band M" : [0,0,0,157,58], "Ritualist's Treasured Ring LFR" : [0,116,34,0,0], "Ritualist's Treasured Ring N" : [0,133,39,0,0],"Ritualist's Treasured Ring H" : [0,149,44,0,0], "Ritualist's Treasured Ring M" : [0,165,49,0,0],  "Most Regal Signet of Sire Denathrius LFR" : [0,128,0,0,34], "Most Regal Signet of Sire Denathrius N" : [0,144,0,0,39], "Most Regal Signet of Sire Denathrius H" : [0,161,0,0,44], "Most Regal Signet of Sire Denathrius M" : [0,178,0,0,48]}


Trink1 = {"T1" : [0,0,0,0,45], "Glowing Endmire Stinger" : [0,0,0,0,45], "test_trink1" : [90,0,0,0,0], "Inscrutable Quantum Device HD" : [46,0,0,0,0], "Inscrutable Quantum Device MD" : [52,0,0,0,0], "Sunblood Amethyst HD" : [0,72,0,0,0],  "Sunblood Amethyst MD" : [0,79,0,0,0], "Unbound Changeling HD" : [46,0,0,0,0], "Unbound Changeling MD" : [52,0,0,0,0], "Infinitely Divisible Ooze HD" : [46,0,0,0,0],  "Infinitely Divisible Ooze MD" : [52,0,0,0,0], "Overflowing Anima Cage HD" : [46,0,0,0,0],  "Overflowing Anima Cage MD" : [52,0,0,0,0], "Empyreal Ordnance HD" : [0,0,0,0,72],
 "Empyreal Ordnance MD" : [0,0,0,0,79], "Satchel of Misbegotten Minions HD" : [46,0,0,0,0], "Satchel of Misbegotten Minions MD" : [52,0,0,0,0], "Soulletting Ruby HD" : [46,0,0,0,0], "Soulletting Ruby MD" : [52,0,0,0,0], "Soul Igniter LFR" : [54,0,0,0,0],  "Soul Igniter N" : [61,0,0,0,0], "Soul Igniter H" : [69,0,0,0,0], "Soul Igniter M" : [77,0,0,0,0], "Glyph of Assimilation LFR" : [54,0,0,0,0], "Glyph of Assimilation N" : [61,0,0,0,0], "Glyph of Assimilation H" : [69,0,0,0,0], "Glyph of Assimilation M" : [77,0,0,0,0], "Macabre Sheet Music LFR" : [54,0,0,0,0], "Macabre Sheet Music N" : [61,0,0,0,0], "Macabre Sheet Music H" : [69,0,0,0,0], "Macabre Sheet Music M" : [77,0,0,0,0], "Cabalist's Hymnal LFR" : [57,0,0,0,0], "Cabalist's Hymnal N" : [65,0,0,0,0], "Cabalist's Hymnal H" : [73,0,0,0,0], "Cabalist's Hymnal M" : [83,0,0,0,0], "Dreadfire Vessel LFR" : [57,0,0,0,0], "Dreadfire Vessel N" : [65,0,0,0,0], "Dreadfire Vessel H" : [73,0,0,0,0], "Dreadfire Vessel M" : [83,0,0,0,0]}


Trink2 = {"T2" : [28,0,0,0,0], "Vial of Caustic Liquid" : [28,0,0,0,0], "test_trink2" : [0,270,0,0,0], "Inscrutable Quantum Device HD" : [46,0,0,0,0], "Inscrutable Quantum Device MD" : [52,0,0,0,0], "Sunblood Amethyst HD" : [0,72,0,0,0],  "Sunblood Amethyst MD" : [0,79,0,0,0], "Unbound Changeling HD" : [46,0,0,0,0], "Unbound Changeling MD" : [52,0,0,0,0], "Infinitely Divisible Ooze HD" : [46,0,0,0,0],  "Infinitely Divisible Ooze MD" : [52,0,0,0,0], "Overflowing Anima Cage HD" : [46,0,0,0,0],  "Overflowing Anima Cage MD" : [52,0,0,0,0], "Empyreal Ordnance HD" : [0,0,0,0,72],
 "Empyreal Ordnance MD" : [0,0,0,0,79], "Satchel of Misbegotten Minions HD" : [46,0,0,0,0], "Satchel of Misbegotten Minions MD" : [52,0,0,0,0], "Soulletting Ruby HD" : [46,0,0,0,0], "Soulletting Ruby MD" : [52,0,0,0,0],  "Soul Igniter LFR" : [54,0,0,0,0],  "Soul Igniter N" : [61,0,0,0,0], "Soul Igniter H" : [69,0,0,0,0], "Soul Igniter M" : [77,0,0,0,0], "Glyph of Assimilation LFR" : [54,0,0,0,0], "Glyph of Assimilation N" : [61,0,0,0,0], "Glyph of Assimilation H" : [69,0,0,0,0], "Glyph of Assimilation M" : [77,0,0,0,0],  "Macabre Sheet Music LFR" : [54,0,0,0,0], "Macabre Sheet Music N" : [61,0,0,0,0], "Macabre Sheet Music H" : [69,0,0,0,0], "Macabre Sheet Music M" : [77,0,0,0,0], "Cabalist's Hymnal LFR" : [57,0,0,0,0], "Cabalist's Hymnal N" : [65,0,0,0,0], "Cabalist's Hymnal H" : [73,0,0,0,0], "Cabalist's Hymnal M" : [83,0,0,0,0], "Dreadfire Vessel LFR" : [57,0,0,0,0], "Dreadfire Vessel N" : [65,0,0,0,0], "Dreadfire Vessel H" : [73,0,0,0,0], "Dreadfire Vessel M" : [83,0,0,0,0]}



MainHand = {"MH" : [113,0,16,0,19], "Sinfall Inquisitor's Dagger" : [113,0,16,0,19], "none" : [0,0,0,0,0], "test_mainhand" : [115,90,0,90,0], "Scithewood Scepter HD" : [141,0,17,0,33], "Scithewood Scepter MD" : [159,0,19,0,36], "Surgical Pustule Extractor HD" : [141,0,31,0,18],  "Surgical Pustule Extractor MD" : [159,0,35,0,21], "Fleshcrafter's Knife HD" : [141,29,0,20,0],  "Fleshcrafter's Knife MD" : [159,32,0,22,0]}


OffHand = {"OH" : [65,0,0,18,25], "Waylight Defender" : [65,0,0,18,25], "none" : [0,0,0,0,0], "test_offhand" : [55,0,90,0,90], "Acidslough Bulwark HD" : [74,20,0,0,31], "Acidslough Bulwark MD" : [84,21,0,0,33], "Encrusted Canopic Lid HD" : [74,0,29,20,0], "Encrusted Canopic Lid MD" : [84,0,32,22,0], "Barricade of the Endless Empire HD" : [74,31,18,0,0],  "Barricade of the Endless Empire MD" : [84,35,21,0,0]}

TwoHand = {"none" : [0,0,0,0,0],"test_twohand" : [180,60,0,0,60], "Whizblast Walking Stick HD" : [218,0,0,40,63], "Whizblast Walking Stick MD" : [245,0,0,44,68], "Nathrian Ferula HD" : [218,59,42,0,0], "Nathrian Ferula MD" : [245,65,45,0,0], "Lakali's Spire of Knowledge HD" : [218,0,0,66,36], "Lakali's Spire of Knowledge MD" : [245,0,0,73,39]}

gemType = {"Versatile Jewel Cluster" : [0,0,0,16,0], "Quick Jewel Cluster" : [0,16,0,0,0]}
enchantType = {}

statCollector = []
DPSCollector = []

while simCollector == True:

    characterPage = []
    gearSelection = True
    while gearSelection == True:
        helmSlot = str(input("What Helmet are you wearing?"))
        if helmSlot in Helm:
            gearSelection = False
            helmSlot = Helm[helmSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(helmSlot)


    while gearSelection == True:
        neckSlot = str(input("What Necklace are you wearing?"))
        if neckSlot in Neck:
            gearSelection = False
            neckSlot = Neck[neckSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(neckSlot)


    while gearSelection == True:
        shoulderSlot = str(input("What Shoulders are you wearing?"))
        if shoulderSlot in Shoulder:
            gearSelection = False
            shoulderSlot = Shoulder[shoulderSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(shoulderSlot)

    while gearSelection == True:
        backSlot = str(input("What Back are you wearing?"))
        if backSlot in Back:
            gearSelection = False
            backSlot = Back[backSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(backSlot)

    while gearSelection == True:
        chestSlot = str(input("What Chestpiece are you wearing?"))
        if chestSlot in Chest:
            gearSelection = False
            chestSlot = Chest[chestSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(chestSlot)

    while gearSelection == True:
        wristSlot = str(input("What Wrist are you wearing?"))
        if wristSlot in Wrist:
            gearSelection = False
            wristSlot = Wrist[wristSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(wristSlot)

    while gearSelection == True:
        handsSlot = str(input("What Hands are you wearing?"))
        if handsSlot in Hands:
            gearSelection = False
            handsSlot = Hands[handsSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(handsSlot)

    while gearSelection == True:
        beltSlot = str(input("What Waist are you wearing?"))
        if beltSlot in Waist:
            gearSelection = False
            beltSlot = Waist[beltSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(beltSlot)
    

   
    while gearSelection == True:
        legsSlot = str(input("What Leggings are you wearing?"))
        if legsSlot in Legs:
            gearSelection = False
            legsSlot = Legs[legsSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(legsSlot)

    while gearSelection == True:
        feetSlot = str(input("What Feet are you wearing?"))
        if feetSlot in Feet:
            gearSelection = False
            feetSlot = Feet[feetSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(feetSlot)

    while gearSelection == True:
        finger1Slot = str(input("What Ring 1 are you wearing?"))
        if finger1Slot in Finger1:
            gearSelection = False
            finger1Slot = Finger1[finger1Slot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(finger1Slot)

    while gearSelection == True:
        finger2Slot = str(input("What Ring 2 are you wearing?"))
        if finger2Slot in Finger2:
            gearSelection = False
            finger2Slot = Finger2[finger2Slot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(finger2Slot)

    
    while gearSelection == True:
        trinket1Slot = str(input("What Trinket 1 are you wearing?"))
        if trinket1Slot in Trink1:
            gearSelection = False
            trinket1Slot = Trink1[trinket1Slot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(trinket1Slot)

    
    while gearSelection == True:
        trinket2Slot = str(input("What Trinket 2 are you wearing?"))
        if trinket2Slot in Trink2:
            gearSelection = False
            trinket2Slot = Trink2[trinket2Slot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(trinket2Slot)

   
    while gearSelection == True:
        mainhandSlot = str(input("What Mainhand are you wearing? (type 'none' if none)"))
        if mainhandSlot in MainHand:
            gearSelection = False
            mainhandSlot = MainHand[mainhandSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(mainhandSlot)

    while gearSelection == True:
        offhandSlot = str(input("What Offhand are you wearing? (type 'none' if none"))
        if offhandSlot in OffHand:
            gearSelection = False
            offhandSlot = OffHand[offhandSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(offhandSlot)

    while gearSelection == True:
        twohandSlot = str(input("What Twohander are you wearing? (type 'none' if none"))
        if twohandSlot in TwoHand:
            gearSelection = False
            twohandSlot = TwoHand[twohandSlot]
        else:
            gearSelection = True
    gearSelection = True
    characterPage.append(twohandSlot)


    int_sum = 0
    haste_sum = 0
    crit_sum = 0
    vers_sum = 0
    mastery_sum = 0
    index_change = 0
    totalStats = []

    haste_num1 = 0
    haste_num2 = 0
    haste_num3 = 0
    haste_num4 = 0
    haste_num5 = 0
    crit_num1 = 0
    crit_num2 = 0
    crit_num3 = 0
    crit_num4 = 0
    crit_num5 = 0
    vers_num1 = 0
    vers_num2 = 0
    vers_num3 = 0
    vers_num4 = 0
    vers_num5 = 0
    mastery_num1 = 0
    mastery_num2 = 0
    mastery_num3 = 0
    mastery_num4 = 0
    mastery_num5 = 0

    gemStats1 = 0
    gemStats2 = 0
    gemNum1 = int(input("How many Versatile Jewel Clusters do you have?"))
    if gemNum1 > 0:
        gemStats1 = gemType["Versatile Jewel Cluster"][3] * gemNum1
    gemNum2 = int(input("How many Quick Jewel Clusters do you have?"))
    if gemNum2 > 0:
        gemStats2 = gemType["Quick Jewel Cluster"][1] * gemNum2


    totalSlots_1h=14
    for _ in range(0,totalSlots_1h+2):
        int_sum = int_sum + float(characterPage[index_change][0])
        haste_sum = haste_sum + float(characterPage[index_change][1])
        crit_sum = crit_sum + float(characterPage[index_change][2])
        vers_sum = vers_sum + float(characterPage[index_change][3])
        mastery_sum = mastery_sum + float(characterPage[index_change][4])
        index_change = index_change + 1

    haste_sum = haste_sum + gemStats2
    vers_sum = vers_sum + gemStats1

        
    totalStats.append(int_sum)
    totalStats.append(haste_sum)
    totalStats.append(crit_sum)
    totalStats.append(vers_sum)
    totalStats.append(mastery_sum)

        
    totalStats[0] = (totalStats[0] + 449) + ((totalStats[0] + 449) * 0.05)
    totalStats[1] = totalStats[1] * 0.0303
    totalStats[2] = (totalStats[2] * 0.0286) + 5.0
    totalStats[3] = totalStats[3] * 0.0250
    totalStats[4] = (totalStats[4] * 0.0536) + 15.0


        
     


        
    if totalStats[1] >= 30 and totalStats[1] <= 39:
        haste_num1 = (totalStats[1]%30) - ((totalStats[1]%30) * 0.10)
        totalStats[1] = 30 + haste_num1
    elif totalStats[1] > 39 and totalStats[1] <= 47:
        haste_num2 = (totalStats[1]%39) - ((totalStats[1]%39) * 0.20)
        haste_num2 =  haste_num2 + (9 - (9 * 0.10))
        totalStats[1] = 30 + haste_num2
    elif totalStats[1] > 47 and totalStats[1] <= 54:
        haste_num3 = (totalStats[1]%47) - ((totalStats[1]%47) * 0.30)
        haste_num3 = haste_num3 + (8 - (8 * 0.20)) 
        haste_num3 = haste_num3 + (9 - (9 * 0.10))
        totalStats[1] = 30 + haste_num3
    elif totalStats[1] > 54 and totalStats[1] <= 66:
        haste_num4 = (totalStats[1]%54) - ((totalStats[1]%54) * 0.40)
        haste_num4 = haste_num4 + (7 - (7 * 0.30))
        haste_num4 = haste_num4 + (8 - (8 * 0.20))
        haste_num4 = haste_num4 + (9 - (9 * 0.10))
        totalStats[1] = 30 + haste_num4
    elif totalStats[1] > 66 and totalStats[1] <= 122:
        haste_num5 = (totalStats[1]%66) - ((totalStats[1]%66) * 0.50)
        haste_num5 = haste_num5 + (12 - (12 * 0.40))
        haste_num5 = haste_num5 + (7 - (7 * 0.30))
        haste_num5 = haste_num5 + (8 - (8 * 0.20))
        haste_num5 = haste_num5 + (9 - (9 * 0.10))
        totalStats[1] = 30 + haste_num5
    else:
        totalStats[1] = totalStats[1]

            
    if  totalStats[2] >= 30 and totalStats[2] <= 39:
        crit_num1 = (totalStats[2]%30) - ((totalStats[2]%30) * 0.10)
        totalStats[2] = 30 + crit_num1
    elif totalStats[2] > 39 and totalStats[2] <= 47:
        crit_num2 = (totalStats[2]%39) - ((totalStats[2]%39) * 0.20)
        crit_num2 =  crit_num2 + (9 - (9 * 0.10))
        totalStats[2] = 30 + crit_num2
    elif totalStats[2] > 47 and totalStats[2] <= 54:
        crit_num3 = (totalStats[2]%47) - ((totalStats[2]%47) * 0.30)
        crit_num3 = crit_num3 + (8 - (8 * 0.20)) 
        crit_num3 = crit_num3 + (9 - (9 * 0.10))
        totalStats[2] = 30 + crit_num3
    elif totalStats[2] > 54 and totalStats[2] <= 66:
        crit_num4 = (totalStats[2]%54) - ((totalStats[2]%54) * 0.40)
        crit_num4 = crit_num4 + (7 - (7 * 0.30))
        crit_num4 = crit_num4 + (8 - (8 * 0.20))
        crit_num4 = crit_num4 + (9 - (9 * 0.10))
        totalStats[2] = 30 + crit_num4
    elif totalStats[2] > 66 and totalStats[2] <= 122:
        crit_num5 = (totalStats[2]%66) - ((totalStats[2]%66) * 0.50)
        crit_num5 = crit_num5 + (12 - (12 * 0.40))
        crit_num5 = crit_num5 + (7 - (7 * 0.30))
        crit_num5 = crit_num5 + (8 - (8 * 0.20))
        crit_num5 = crit_num5 + (9 - (9 * 0.10))
        totalStats[2] = 30 + crit_num5
    else:
        totalStats[2] = totalStats[2]
        
                
                
    if totalStats[3] >= 30 and totalStats[3] <= 39:
        vers_num1 = (totalStats[3]%30) - ((totalStats[3]%30) * 0.10)
        totalStats[3] = 30 + vers_num1
    elif totalStats[3] > 39 and totalStats[3] <= 47:
        vers_num2 = (totalStats[3]%39) - ((totalStats[3]%39) * 0.20)
        vers_num2 =  vers_num2 + (9 - (9 * 0.10))
        totalStats[3] = 30 + vers_num2
    elif totalStats[3] > 47 and totalStats[3] <= 54:
        vers_num3 = (totalStats[3]%47) - ((totalStats[3]%47) * 0.30)
        vers_num3 = vers_num3 + (8 - (8 * 0.20)) 
        vers_num3 = vers_num3 + (9 - (9 * 0.10))
        totalStats[3] = 30 + vers_num3
    elif totalStats[3] > 54 and totalStats[3] <= 66:
        vers_num4 = (totalStats[3]%54) - ((totalStats[3]%54) * 0.40)
        vers_num4 = vers_num4 + (7 - (7 * 0.30))
        vers_num4 = vers_num4 + (8 - (8 * 0.20))
        vers_num4 = vers_num4 + (9 - (9 * 0.10))
        totalStats[3] = 30 + vers_num4
    elif totalStats[3] > 66 and totalStats[3] <= 122:
        vers_num5 = (totalStats[3]%66) - ((totalStats[3]%66) * 0.50)
        vers_num5 = vers_num5 + (12 - (12 * 0.40))
        vers_num5 = vers_num5 + (7 - (7 * 0.30))
        vers_num5 = vers_num5 + (8 - (8 * 0.20))
        vers_num5 = vers_num5 + (9 - (9 * 0.10))
        totalStats[3] = 30 + vers_num5
    else:
        totalStats[3] = totalStats[3]
        
                
                
    if totalStats[4] >= 30 and totalStats[4] <= 39:
        mastery_num1 = (totalStats[4]%30) - ((totalStats[4]%30) * 0.10)
        totalStats[4] = 30 + mastery_num1
    elif totalStats[4] > 39 and totalStats[4] <= 47:
        mastery_num2 = (totalStats[4]%39) - ((totalStats[4]%39) * 0.20)
        mastery_num2 =  mastery_num2 + (9 - (9 * 0.10))
        totalStats[4] = 30 + mastery_num2
    elif totalStats[4] > 47 and totalStats[4] <= 54:
        mastery_num3 = (totalStats[4]%47) - ((totalStats[4]%47) * 0.30)
        mastery_num3 = mastery_num3 + (8 - (8 * 0.20)) 
        mastery_num3 = mastery_num3 + (9 - (9 * 0.10))
        totalStats[4] = 30 + mastery_num3
    elif totalStats[4] > 54 and totalStats[4] <= 66:
        mastery_num4 = (totalStats[4]%54) - ((totalStats[4]%54) * 0.40)
        mastery_num4 = mastery_num4 + (7 - (7 * 0.30))
        mastery_num4 = mastery_num4 + (8 - (8 * 0.20))
        mastery_num4 = mastery_num4 + (9 - (9 * 0.10))
        totalStats[4] = 30 + mastery_num4
    elif totalStats[4] > 66 and totalStats[4] <= 122:
        mastery_num5 = (totalStats[4]%66) - ((totalStats[4]%66) * 0.50)
        mastery_num5 = mastery_num5 + (12 - (12 * 0.40))
        mastery_num5 = mastery_num5 + (7 - (7 * 0.30))
        mastery_num5 = mastery_num5 + (8 - (8 * 0.20))
        mastery_num5 = mastery_num5 + (9 - (9 * 0.10))
        totalStats[4] = 30 + mastery_num5
    else:
        totalStats[4] = totalStats[4]
    "print(totalStats)"

    statPercents = []
    statPercents.append(totalStats[0])
    haste_percent = totalStats[1]/100
    statPercents.append(haste_percent)
    crit_percent = totalStats[2]/100
    statPercents.append(crit_percent)
    vers_percent= totalStats[3]/100
    statPercents.append(vers_percent)
    mastery_percent = totalStats[4]/100
    statPercents.append(mastery_percent)

    "print(statPercents)"
    statCollector.append(statPercents)
    statCons = statPercents
    
    intCons = totalStats[0]
    hastCons = totalStats[1]/100
    critCons = totalStats[2]/100
    versCons = totalStats[3]/100
    mastCons = totalStats[4]/100

    
    ovrSTATS = []




    avgDPS = []
    avgHAST = []
    avgCRIT = []
    avgVERS = []
    avgMAST = []
    avgINTL = []
    avgTOTAL = []


    tot_dmg = 0.0

    

    maelstrom = 0.0

    lengthUser = float(input("How long do you want to sim? In minutes"))
    time = float(lengthUser) * 60.0
    fight_time = time

    castOrig = 2.0 - (2.0 * hastCons)
    cast = castOrig
    
    GCD = 1.5 - (haste_sum * 0.0004)
    hasteMultiplier = haste_sum + (haste_sum * 0.035)
    GCDHASTE = 1.5 - (hasteMultiplier * 0.0004)
    SP = intCons

    numTrgts = 1

    

    EchShock_cd = 30.0
    Ascendence_cd = 180.0
    Felemental_cd = 150.0
    FlS_cd = 6.0
    LB1_cd = 8.0
    LB2_cd = 8.0
    IF_cd = 30.0

    FlS_dur = 18.0

    LiB_dmg = (SP * 0.95) + (SP * 0.95) * versCons 
    LiB_crit = LiB_dmg * 2.50



    LB_dmg = (SP * 1.08) + (SP * 1.08) * versCons
    LB_crit = LB_dmg * 2.50


    IF_dmg = (SP * 0.825) + (SP * 0.825) * versCons
    IF_crit = IF_dmg * 2.50

    CL_dmg = ((SP * 0.47) + (SP * 0.47) * versCons) * numTrgts
    CL_crit = CL_dmg * 2.50

    FrS_dmg = (SP * 0.45) + (SP * 0.45) * versCons
    FrS_crit = FrS_dmg * 2.50

    EQ_dmg = ((SP * 0.23) + (SP * 0.23) * versCons) * numTrgts
    EQ_crit = EQ_dmg * 2.50

    echS_dmg = (SP * 0.65) + (SP * 0.65) * versCons
    echS_crit = echS_dmg * 2.50

    EaS_dmg = (SP * 2.10) + (SP * 2.10) * versCons
    EaS_crit = EaS_dmg * 2.50

    FlS_dmg = (SP * 0.195) + (SP * 0.195) * versCons
    FlS_crit = FlS_dmg * 2.50

    FlS_tick = (SP * 0.058) + (SP * 0.058) * versCons
    FlS_tick_crit = FlS_tick * 2.50

    









    FlS_applied = False
    FlS_timer = 0

    LB1_applied = False
    LB1_timer = 0
    LB2_applied = False
    LB2_timer = 0

    IF_applied = False
    IF_timer = 0

    echS_timer = 0

    Asc_timer = 0
    Asc_applied = False

    EaS_applied = False
    EQ_applied = False


    GCD_loss = (time/30) * GCD
    "print(GCD_loss)"
    time = time - GCD_loss
    fight_time = time
    time = fight_time

        
    DPS_list = []

    sim_count = int(input("How many sims would you like to run?"))
    
    for _ in range(1,sim_count+1):
        LiB_dmg = (SP * 0.95) + (SP * 0.95) * versCons 
        LiB_crit = LiB_dmg * 2.50
        "print(LiB_dmg)"



        LB_dmg = (SP * 1.08) + (SP * 1.08) * versCons
        LB_crit = LB_dmg * 2.50
        "print(LB_dmg)"


        IF_dmg = (SP * 0.825) + (SP * 0.825) * versCons
        IF_crit = IF_dmg * 2.50
        "print(IF_dmg)"

        CL_dmg = ((SP * 0.47) + (SP * 0.47) * versCons) * numTrgts
        CL_crit = CL_dmg * 2.50
        

        
        FrS_dmg = (SP * 0.45) + (SP * 0.45) * versCons
        FrS_crit = FrS_dmg * 2.50
        "print(FrS_dmg)"

        EQ_dmg = ((SP * 0.23) + (SP * 0.23) * versCons) * numTrgts
        EQ_crit = EQ_dmg * 2.50

        echS_dmg = (SP * 0.65) + (SP * 0.65) * versCons
        echS_crit = echS_dmg * 2.50
        "print(echS_dmg)"

        EaS_dmg = (SP * 2.10) + (SP * 2.10) * versCons
        EaS_crit = EaS_dmg * 2.50
        "print(EaS_dmg)"

        FlS_dmg = (SP * 0.195) + (SP * 0.195) * versCons
        FlS_crit = FlS_dmg * 2.50
        "print(FlS_dmg)"

        FlS_tick = (SP * 0.058) + (SP * 0.058) * versCons
        FlS_tick_crit = FlS_tick * 2.50
        "print(FlS_tick)"
        while time > 0:
            if IF_timer >= 30:
                IF_timer == 0
            if echS_timer >= 30:
                echS_timer = 0
                
            if LB1_timer >= 8:
                LB1_timer = 0
            if LB2_timer >= 8:
                LB2_timer = 0
            if Asc_timer >= 180:
                Asc_timer = 0
            if FlS_timer >= 18:
                FlS_timer = 0
            if  FlS_timer<=18 and FlS_applied == False:
                FlS_applied = True
                time = time - GCD
                FlS_timer = FlS_timer + GCD
                dmg_roll = random.randint(1,100)
                if dmg_roll > 100 - (100 * critCons):
                    tot_dmg = tot_dmg + (FlS_dmg * 2.50)
                    tot_dmg = tot_dmg + (FlS_tick * 18)
                elif dmg_roll < 100 - (100 * critCons):
                    tot_dmg = tot_dmg + FlS_dmg + (FlS_tick * 18)
                if LB1_timer > 0:
                    LB1_timer = LB1_timer + GCD
                if LB2_timer > 0:
                    LB2_timer = LB2_timer + GCD
                if echS_timer > 0 :
                    echS_timer = echS_timer + GCD
                if Asc_timer > 0:
                    Asc_timer = Asc_timer + GCD
                if IF_timer > 0:
                    IF_timer = IF_timer + GCD
            
           
            elif FlS_timer >= 18:
                FlS_applied = False
                FlS_timer = 0
                
            if Asc_timer == 0 and echS_timer == 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                echS_timer = echS_timer + 15
                if Asc_applied == True:
                    tot_dmg = tot_dmg + echS_dmg + LB_crit
                    for i in range(1-9):
                        tot_dmg = tot_dmg + (LB_crit)
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time -15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                    
            elif Asc_timer == 0 and echS_timer > 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                LB1_timer = 0
                LB2_timer = 0
                if Asc_applied == True:
                    for i in range(1-9):
                        tot_dmg = tot_dmg + LB_crit
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time - 15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                        
            
                    
                    
                
                
          

                
                    
                    
            if LB1_timer == 0 or LB2_timer == 0:
                if LB1_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB1_timer = LB1_timer + GCD 
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer +GCD+GCD+cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB2_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 5)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*5)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_tiemr = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast + GCD
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0

                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer= 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                      


                
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + GCD + cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer =0
                        elif maelstrom + 20 >= 60 and LB1_timer == 0 and LB2_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                                
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer  = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*3)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB1_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            
                    
                    
                  

                elif LB2_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer +GCD+GCD+cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB1_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 5)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*5)
                            if LB1_timer >= 8:
                                LB1_timer =0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if Fls_timer >= 18:
                                FlS_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0       
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >=30:
                                     IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                        
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + GCD + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif maelstrom + 20 >= 60 and LB2_timer == 0 and LB1_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB2_timer = LB2_timer + cast + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*3)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB2_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast
                                
                            if LB1_timer >= 8:
                                LB1_timer = 0

                
            else:
                    dmg_roll = random.randint(1,100)
                    if dmg_roll > 100 - (100 * critCons):
                        tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                    elif dmg_roll < 100 - (100 * critCons):
                        tot_dmg = tot_dmg + LiB_dmg
                    time = time - cast
                    LB1_timer = LB1_timer + cast
                    if LB1_timer >= 8:
                        LB1_timer = 0
                    LB2_timer = LB2_timer + cast
                    if LB2_timer >= 8:
                        LB2_timer = 0
                    maelstrom = maelstrom + 8
                    
                    if IF_timer > 0:
                        IF_timer = IF_timer + cast
                        if IF_timer >= 30:
                            IF_timer = 0
                    if FlS_timer > 0:
                        FlS_timer = FlS_timer + cast
                        if FlS_timer >= 18:
                            FlS_timer = 0
                    if Asc_timer > 0:
                        Asc_timer = Asc_timer + cast
                        if Asc_timer >= 180:
                            Asc_timer = 0
                    if echS_timer > 0:
                        echS_timer = echS_timer + cast
                    if echS_timer >= 30:
                        echS_timer = 0



            

            """print(time)
            print(LB1_timer)
            print(LB2_timer)
            print(echS_timer)
            print(Asc_timer)
            print(IF_timer)
            print(FlS_timer)
            print(maelstrom)"""

        tot_dmg = tot_dmg + ((fight_time/34) * LB_crit)
        tot_dmg = tot_dmg + ((tot_dmg * mastCons) * 0.85)
        DPS_base = tot_dmg/fight_time
        "print(DPS_base)"
        DPS_list.append(DPS_base)
        avgDPS.append(DPS_base)
        statPercents[4] = mastCons + 0.035

        FlS_applied = False
        FlS_timer = 0

        LB1_applied = False
        LB1_timer = 0
        LB2_applied = False
        LB2_timer = 0

        IF_applied = False
        IF_timer = 0

        echS_timer = 0

        Asc_timer = 0
        Asc_applied = False

        EaS_applied = False
        EQ_applied = False

        maelstrom = 0


            


        tot_dmg = 0
        time = fight_time

        while time > 0:
            if IF_timer >= 30:
                IF_timer == 0
            if echS_timer >= 30:
                echS_timer = 0
                
            if LB1_timer >= 8:
                LB1_timer = 0
            if LB2_timer >= 8:
                LB2_timer = 0
            if Asc_timer >= 180:
                Asc_timer = 0
            if FlS_timer >= 18:
                FlS_timer = 0
            if  FlS_timer<=18 and FlS_applied == False:
                FlS_applied = True
                time = time - GCD
                FlS_timer = FlS_timer + GCD
                dmg_roll = random.randint(1,100)
                if dmg_roll > 100 - (100 * critCons):
                    tot_dmg = tot_dmg + (FlS_dmg * 2.50)
                    tot_dmg = tot_dmg + (FlS_tick * 18)
                elif dmg_roll < 100 - (100 * critCons):
                    tot_dmg = tot_dmg + FlS_dmg + (FlS_tick * 18)
                if LB1_timer > 0:
                    LB1_timer = LB1_timer + GCD
                if LB2_timer > 0:
                    LB2_timer = LB2_timer + GCD
                if echS_timer > 0 :
                    echS_timer = echS_timer + GCD
                if Asc_timer > 0:
                    Asc_timer = Asc_timer + GCD
                if IF_timer > 0:
                    IF_timer = IF_timer + GCD
            
           
            elif FlS_timer >= 18:
                FlS_applied = False
                FlS_timer = 0
                
            if Asc_timer == 0 and echS_timer == 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                echS_timer = echS_timer + 15
                if Asc_applied == True:
                    tot_dmg = tot_dmg + echS_dmg + LB_crit
                    for i in range(1-9):
                        tot_dmg = tot_dmg + (LB_crit)
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time -15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                    
            elif Asc_timer == 0 and echS_timer > 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                LB1_timer = 0
                LB2_timer = 0
                if Asc_applied == True:
                    for i in range(1-9):
                        tot_dmg = tot_dmg + LB_crit
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time - 15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                        
            
                    
                    
                
                
          

                
                    
                    
            if LB1_timer == 0 or LB2_timer == 0:
                if LB1_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB1_timer = LB1_timer + GCD 
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer +GCD+GCD+cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB2_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 5)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*5)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_tiemr = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast + GCD
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0

                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer= 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                      


                
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + GCD + cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer =0
                        elif maelstrom + 20 >= 60 and LB1_timer == 0 and LB2_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                                
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer  = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*3)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB1_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            
                    
                    
                  

                elif LB2_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer +GCD+GCD+cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB1_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 5)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*5)
                            if LB1_timer >= 8:
                                LB1_timer =0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if Fls_timer >= 18:
                                FlS_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0       
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >=30:
                                     IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                        
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + GCD + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif maelstrom + 20 >= 60 and LB2_timer == 0 and LB1_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB2_timer = LB2_timer + cast + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*3)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB2_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast
                                
                            if LB1_timer >= 8:
                                LB1_timer = 0

                
            else:
                    dmg_roll = random.randint(1,100)
                    if dmg_roll > 100 - (100 * critCons):
                        tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                    elif dmg_roll < 100 - (100 * critCons):
                        tot_dmg = tot_dmg + LiB_dmg
                    time = time - cast
                    LB1_timer = LB1_timer + cast
                    if LB1_timer >= 8:
                        LB1_timer = 0
                    LB2_timer = LB2_timer + cast
                    if LB2_timer >= 8:
                        LB2_timer = 0
                    maelstrom = maelstrom + 8
                    
                    if IF_timer > 0:
                        IF_timer = IF_timer + cast
                        if IF_timer >= 30:
                            IF_timer = 0
                    if FlS_timer > 0:
                        FlS_timer = FlS_timer + cast
                        if FlS_timer >= 18:
                            FlS_timer = 0
                    if Asc_timer > 0:
                        Asc_timer = Asc_timer + cast
                        if Asc_timer >= 180:
                            Asc_timer = 0
                    if echS_timer > 0:
                        echS_timer = echS_timer + cast
                    if echS_timer >= 30:
                        echS_timer = 0


                        

        tot_dmg = tot_dmg + ((fight_time/34) * LB_crit)
        tot_dmg = tot_dmg + ((tot_dmg * statPercents[4]) * 0.85)

        DPS_mastery = tot_dmg/fight_time
        "print(DPS_mastery)"
        DPS_list.append(DPS_mastery)
        avgMAST.append(DPS_mastery)

        tot_dmg = 0
        time = fight_time
        statPercents[4] = mastCons 
        statPercents[3] = versCons + 0.035

        """LiB_dmg = (SP * 0.95) + (SP * 0.95) * statPercents[3] 
        LiB_crit = LiB_dmg * 2.50



        LB_dmg = (SP * 1.08) + (SP * 1.08) * statPercents[3]
        LB_crit = LB_dmg * 2.50


        IF_dmg = (SP * 0.825) + (SP * 0.825) * statPercents[3]
        IF_crit = IF_dmg * 2.50

        CL_dmg = ((SP * 0.47) + (SP * 0.47) * statPercents[3]) * numTrgts
        CL_crit = CL_dmg * 2.50

        FrS_dmg = (SP * 0.45) + (SP * 0.45) * statPercents[3]
        FrS_crit = FrS_dmg * 2.50

        EQ_dmg = ((SP * 0.23) + (SP * 0.23) * statPercents[3]) * numTrgts
        EQ_crit = EQ_dmg * 2.50

        echS_dmg = (SP * 0.65) + (SP * 0.65) * statPercents[3]
        echS_crit = echS_dmg * 2.50

        EaS_dmg = (SP * 2.10) + (SP * 2.10) * statPercents[3]
        EaS_crit = EaS_dmg * 2.50

        FlS_dmg = (SP * 0.195) + (SP * 0.195) * statPercents[3]
        FlS_crit = FlS_dmg * 2.50

        FlS_tick = (SP * 0.058) + (SP * 0.058) * statPercents[3]
        FlS_tick_crit = FlS_tick * 2.50"""



        FlS_applied = False
        FlS_timer = 0

        LB1_applied = False
        LB1_timer = 0
        LB2_applied = False
        LB2_timer = 0

        IF_applied = False
        IF_timer = 0

        echS_timer = 0

        Asc_timer = 0
        Asc_applied = False

        EaS_applied = False
        EQ_applied = False

        maelstrom = 0


        while time > 0:
            if IF_timer >= 30:
                IF_timer == 0
            if echS_timer >= 30:
                echS_timer = 0
                
            if LB1_timer >= 8:
                LB1_timer = 0
            if LB2_timer >= 8:
                LB2_timer = 0
            if Asc_timer >= 180:
                Asc_timer = 0
            if FlS_timer >= 18:
                FlS_timer = 0
            if  FlS_timer<=18 and FlS_applied == False:
                FlS_applied = True
                time = time - GCD
                FlS_timer = FlS_timer + GCD
                dmg_roll = random.randint(1,100)
                if dmg_roll > 100 - (100 * critCons):
                    tot_dmg = tot_dmg + (FlS_dmg * 2.50)
                    tot_dmg = tot_dmg + (FlS_tick * 18)
                elif dmg_roll < 100 - (100 * critCons):
                    tot_dmg = tot_dmg + FlS_dmg + (FlS_tick * 18)
                if LB1_timer > 0:
                    LB1_timer = LB1_timer + GCD
                if LB2_timer > 0:
                    LB2_timer = LB2_timer + GCD
                if echS_timer > 0 :
                    echS_timer = echS_timer + GCD
                if Asc_timer > 0:
                    Asc_timer = Asc_timer + GCD
                if IF_timer > 0:
                    IF_timer = IF_timer + GCD
            
           
            elif FlS_timer >= 18:
                FlS_applied = False
                FlS_timer = 0
                
            if Asc_timer == 0 and echS_timer == 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                echS_timer = echS_timer + 15
                if Asc_applied == True:
                    tot_dmg = tot_dmg + echS_dmg + LB_crit
                    for i in range(1-9):
                        tot_dmg = tot_dmg + (LB_crit)
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time -15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                    
            elif Asc_timer == 0 and echS_timer > 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                LB1_timer = 0
                LB2_timer = 0
                if Asc_applied == True:
                    for i in range(1-9):
                        tot_dmg = tot_dmg + LB_crit
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time - 15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                        
            
                    
                    
                
                
          

                
                    
                    
            if LB1_timer == 0 or LB2_timer == 0:
                if LB1_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB1_timer = LB1_timer + GCD 
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer +GCD+GCD+cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB2_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 5)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*5)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_tiemr = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast + GCD
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0

                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer= 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                      


                
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + GCD + cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer =0
                        elif maelstrom + 20 >= 60 and LB1_timer == 0 and LB2_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                                
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer  = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*3)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB1_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            
                    
                    
                  

                elif LB2_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer +GCD+GCD+cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB1_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 5)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*5)
                            if LB1_timer >= 8:
                                LB1_timer =0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if Fls_timer >= 18:
                                FlS_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0       
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >=30:
                                     IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                        
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + GCD + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif maelstrom + 20 >= 60 and LB2_timer == 0 and LB1_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB2_timer = LB2_timer + cast + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*3)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB2_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast
                                
                            if LB1_timer >= 8:
                                LB1_timer = 0

                
            else:
                    dmg_roll = random.randint(1,100)
                    if dmg_roll > 100 - (100 * critCons):
                        tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                    elif dmg_roll < 100 - (100 * critCons):
                        tot_dmg = tot_dmg + LiB_dmg
                    time = time - cast
                    LB1_timer = LB1_timer + cast
                    if LB1_timer >= 8:
                        LB1_timer = 0
                    LB2_timer = LB2_timer + cast
                    if LB2_timer >= 8:
                        LB2_timer = 0
                    maelstrom = maelstrom + 8
                    
                    if IF_timer > 0:
                        IF_timer = IF_timer + cast
                        if IF_timer >= 30:
                            IF_timer = 0
                    if FlS_timer > 0:
                        FlS_timer = FlS_timer + cast
                        if FlS_timer >= 18:
                            FlS_timer = 0
                    if Asc_timer > 0:
                        Asc_timer = Asc_timer + cast
                        if Asc_timer >= 180:
                            Asc_timer = 0
                    if echS_timer > 0:
                        echS_timer = echS_timer + cast
                    if echS_timer >= 30:
                        echS_timer = 0


        tot_dmg = tot_dmg + ((fight_time/34) * LB_crit)
        tot_dmg = tot_dmg + ((tot_dmg * mastCons) * 0.85) + (tot_dmg * statPercents[3])

        DPS_vers = tot_dmg/fight_time
        "print(DPS_vers)"
        DPS_list.append(DPS_vers)
        avgVERS.append(DPS_vers)

        statPercents[3] = versCons 
        statPercents[2] = critCons + 0.035

        LiB_dmg = (SP * 0.95) + (SP * 0.95) * versCons 
        LiB_crit = LiB_dmg * 2.50



        LB_dmg = (SP * 1.08) + (SP * 1.08) * versCons
        LB_crit = LB_dmg * 2.50


        IF_dmg = (SP * 0.825) + (SP * 0.825) * versCons
        IF_crit = IF_dmg * 2.50

        CL_dmg = ((SP * 0.47) + (SP * 0.47) * versCons) * numTrgts
        CL_crit = CL_dmg * 2.50

        FrS_dmg = (SP * 0.45) + (SP * 0.45) * versCons
        FrS_crit = FrS_dmg * 2.50

        EQ_dmg = ((SP * 0.23) + (SP * 0.23) * versCons) * numTrgts
        EQ_crit = EQ_dmg * 2.50

        echS_dmg = (SP * 0.65) + (SP * 0.65) * versCons
        echS_crit = echS_dmg * 2.50

        EaS_dmg = (SP * 2.10) + (SP * 2.10) * versCons
        EaS_crit = EaS_dmg * 2.50

        FlS_dmg = (SP * 0.195) + (SP * 0.195) * versCons
        FlS_crit = FlS_dmg * 2.50

        FlS_tick = (SP * 0.058) + (SP * 0.058) * versCons
        FlS_tick_crit = FlS_tick * 2.50


        FlS_applied = False
        FlS_timer = 0

        LB1_applied = False
        LB1_timer = 0
        LB2_applied = False
        LB2_timer = 0

        IF_applied = False
        IF_timer = 0

        echS_timer = 0

        Asc_timer = 0
        Asc_applied = False

        EaS_applied = False
        EQ_applied = False

        maelstrom = 0


        tot_dmg = 0
        time = fight_time

        while time > 0:
            if IF_timer >= 30:
                IF_timer == 0
            if echS_timer >= 30:
                echS_timer = 0
                
            if LB1_timer >= 8:
                LB1_timer = 0
            if LB2_timer >= 8:
                LB2_timer = 0
            if Asc_timer >= 180:
                Asc_timer = 0
            if FlS_timer >= 18:
                FlS_timer = 0
            if  FlS_timer<=18 and FlS_applied == False:
                FlS_applied = True
                time = time - GCD
                FlS_timer = FlS_timer + GCD
                dmg_roll = random.randint(1,100)
                if dmg_roll > 100 - (100 * statPercents[2]):
                    tot_dmg = tot_dmg + (FlS_dmg * 2.50)
                    tot_dmg = tot_dmg + (FlS_tick * 18)
                elif dmg_roll < 100 - (100 * statPercents[2]):
                    tot_dmg = tot_dmg + FlS_dmg + (FlS_tick * 18)
                if LB1_timer > 0:
                    LB1_timer = LB1_timer + GCD
                if LB2_timer > 0:
                    LB2_timer = LB2_timer + GCD
                if echS_timer > 0 :
                    echS_timer = echS_timer + GCD
                if Asc_timer > 0:
                    Asc_timer = Asc_timer + GCD
                if IF_timer > 0:
                    IF_timer = IF_timer + GCD
            
           
            elif FlS_timer >= 18:
                FlS_applied = False
                FlS_timer = 0
                
            if Asc_timer == 0 and echS_timer == 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                echS_timer = echS_timer + 15
                if Asc_applied == True:
                    tot_dmg = tot_dmg + echS_dmg + LB_crit
                    for i in range(1-9):
                        tot_dmg = tot_dmg + (LB_crit)
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time -15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                    
            elif Asc_timer == 0 and echS_timer > 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                LB1_timer = 0
                LB2_timer = 0
                if Asc_applied == True:
                    for i in range(1-9):
                        tot_dmg = tot_dmg + LB_crit
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time - 15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                        
            
                    
                    
                
                
          

                
                    
                    
            if LB1_timer == 0 or LB2_timer == 0:
                if LB1_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB1_timer = LB1_timer + GCD 
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer +GCD+GCD+cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB2_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 5)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*5)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_tiemr = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast + GCD
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0

                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer= 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                      


                
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + GCD + cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer =0
                        elif maelstrom + 20 >= 60 and LB1_timer == 0 and LB2_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                                
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer  = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * statPercentss[2]):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*3)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB1_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            
                    
                    
                  

                elif LB2_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer +GCD+GCD+cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB1_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 5)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*5)
                            if LB1_timer >= 8:
                                LB1_timer =0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if Fls_timer >= 18:
                                FlS_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0       
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >=30:
                                     IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                        
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + GCD + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif maelstrom + 20 >= 60 and LB2_timer == 0 and LB1_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB2_timer = LB2_timer + cast + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * statPercents[2]):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*3)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB2_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast
                                
                            if LB1_timer >= 8:
                                LB1_timer = 0

                
            else:
                    dmg_roll = random.randint(1,100)
                    if dmg_roll > 100 - (100 * statPercents[2]):
                        tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                    elif dmg_roll < 100 - (100 * statPercents[2]):
                        tot_dmg = tot_dmg + LiB_dmg
                    time = time - cast
                    LB1_timer = LB1_timer + cast
                    if LB1_timer >= 8:
                        LB1_timer = 0
                    LB2_timer = LB2_timer + cast
                    if LB2_timer >= 8:
                        LB2_timer = 0
                    maelstrom = maelstrom + 8
                    
                    if IF_timer > 0:
                        IF_timer = IF_timer + cast
                        if IF_timer >= 30:
                            IF_timer = 0
                    if FlS_timer > 0:
                        FlS_timer = FlS_timer + cast
                        if FlS_timer >= 18:
                            FlS_timer = 0
                    if Asc_timer > 0:
                        Asc_timer = Asc_timer + cast
                        if Asc_timer >= 180:
                            Asc_timer = 0
                    if echS_timer > 0:
                        echS_timer = echS_timer + cast
                    if echS_timer >= 30:
                        echS_timer = 0


        tot_dmg = tot_dmg + ((fight_time/34) * LB_crit) + (tot_dmg * critCons/2)
        tot_dmg = tot_dmg + ((tot_dmg * mastCons) * 0.85) 

        DPS_crit = tot_dmg/fight_time
        "print(DPS_crit)"
        DPS_list.append(DPS_crit)
        avgCRIT.append(DPS_crit)

        statPercents[2] = critCons 
        statPercents[1] = hastCons + 0.035
        
       

        cast = castOrig - (2.0 *statPercents[1])
        
                           
        

        FlS_applied = False
        FlS_timer = 0

        LB1_applied = False
        LB1_timer = 0
        LB2_applied = False
        LB2_timer = 0

        IF_applied = False
        IF_timer = 0

        echS_timer = 0

        Asc_timer = 0
        Asc_applied = False

        EaS_applied = False
        EQ_applied = False

        maelstrom = 0

        

        tot_dmg = 0
        time = fight_time 


        while time > 0:
            if IF_timer >= 30:
                IF_timer == 0
            if echS_timer >= 30:
                echS_timer = 0
                
            if LB1_timer >= 8:
                LB1_timer = 0
            if LB2_timer >= 8:
                LB2_timer = 0
            if Asc_timer >= 180:
                Asc_timer = 0
            if FlS_timer >= 18:
                FlS_timer = 0
            if  FlS_timer<=18 and FlS_applied == False:
                FlS_applied = True
                time = time - GCD
                FlS_timer = FlS_timer + GCD
                dmg_roll = random.randint(1,100)
                if dmg_roll > 100 - (100 * critCons):
                    tot_dmg = tot_dmg + (FlS_dmg * 2.50)
                    tot_dmg = tot_dmg + (FlS_tick * 18)
                elif dmg_roll < 100 - (100 * critCons):
                    tot_dmg = tot_dmg + FlS_dmg + (FlS_tick * 18)
                if LB1_timer > 0:
                    LB1_timer = LB1_timer + GCD
                if LB2_timer > 0:
                    LB2_timer = LB2_timer + GCD
                if echS_timer > 0 :
                    echS_timer = echS_timer + GCD
                if Asc_timer > 0:
                    Asc_timer = Asc_timer + GCD
                if IF_timer > 0:
                    IF_timer = IF_timer + GCD
            
           
            elif FlS_timer >= 18:
                FlS_applied = False
                FlS_timer = 0
                
            if Asc_timer == 0 and echS_timer == 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                echS_timer = echS_timer + 15
                if Asc_applied == True:
                    tot_dmg = tot_dmg + echS_dmg + LB_crit
                    for i in range(1-9):
                        tot_dmg = tot_dmg + (LB_crit)
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time -15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                    
            elif Asc_timer == 0 and echS_timer > 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                LB1_timer = 0
                LB2_timer = 0
                if Asc_applied == True:
                    for i in range(1-9):
                        tot_dmg = tot_dmg + LB_crit
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time - 15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                        
            
                    
                    
                
                
          

                
                    
                    
            if LB1_timer == 0 or LB2_timer == 0:
                if LB1_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB1_timer = LB1_timer + GCD 
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer +GCD+GCD+cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB2_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 5)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*5)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_tiemr = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast + GCD
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0

                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer= 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                      


                
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + GCD + cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer =0
                        elif maelstrom + 20 >= 60 and LB1_timer == 0 and LB2_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                                
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer  = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*3)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB1_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            
                    
                    
                  

                elif LB2_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer +GCD+GCD+cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB1_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 5)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*5)
                            if LB1_timer >= 8:
                                LB1_timer =0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if Fls_timer >= 18:
                                FlS_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0       
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >=30:
                                     IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                        
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + GCD + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif maelstrom + 20 >= 60 and LB2_timer == 0 and LB1_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB2_timer = LB2_timer + cast + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*3)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB2_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast
                                
                            if LB1_timer >= 8:
                                LB1_timer = 0

                
            else:
                    dmg_roll = random.randint(1,100)
                    if dmg_roll > 100 - (100 * critCons):
                        tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                    elif dmg_roll < 100 - (100 * critCons):
                        tot_dmg = tot_dmg + LiB_dmg
                    time = time - cast
                    LB1_timer = LB1_timer + cast
                    if LB1_timer >= 8:
                        LB1_timer = 0
                    LB2_timer = LB2_timer + cast
                    if LB2_timer >= 8:
                        LB2_timer = 0
                    maelstrom = maelstrom + 8
                    
                    if IF_timer > 0:
                        IF_timer = IF_timer + cast
                        if IF_timer >= 30:
                            IF_timer = 0
                    if FlS_timer > 0:
                        FlS_timer = FlS_timer + cast
                        if FlS_timer >= 18:
                            FlS_timer = 0
                    if Asc_timer > 0:
                        Asc_timer = Asc_timer + cast
                        if Asc_timer >= 180:
                            Asc_timer = 0
                    if echS_timer > 0:
                        echS_timer = echS_timer + cast
                    if echS_timer >= 30:
                        echS_timer = 0


        tot_dmg = tot_dmg + ((fight_time/34) * LB_crit)
        tot_dmg = tot_dmg + ((tot_dmg * mastCons) * 0.85)

        DPS_haste = tot_dmg/fight_time
        "print(DPS_haste)"
        DPS_list.append(DPS_haste)
        avgHAST.append(DPS_haste)

        "print(intCons)"
        statPercents[0] = intCons + (intCons * 0.035)

        tot_dmg = 0
        time = fight_time
        GCD = GCD

        SP = statPercents[0]
        "print(SP)"
        
        cast = castOrig
        statPercents[1] = hastCons 

        LiB_dmg = (SP * 0.95) + (SP * 0.95) * versCons 
        LiB_crit = LiB_dmg * 2.50



        LB_dmg = (SP * 1.08) + (SP * 1.08) * versCons
        LB_crit = LB_dmg * 2.50


        IF_dmg = (SP * 0.825) + (SP * 0.825) * versCons
        IF_crit = IF_dmg * 2.50

        CL_dmg = ((SP * 0.47) + (SP * 0.47) * versCons) * numTrgts
        CL_crit = CL_dmg * 2.50

        FrS_dmg = (SP * 0.45) + (SP * 0.45) * versCons
        FrS_crit = FrS_dmg * 2.50

        EQ_dmg = ((SP * 0.23) + (SP * 0.23) * versCons) * numTrgts
        EQ_crit = EQ_dmg * 2.50

        echS_dmg = (SP * 0.65) + (SP * 0.65) * versCons
        echS_crit = echS_dmg * 2.50

        EaS_dmg = (SP * 2.10) + (SP * 2.10) * versCons
        EaS_crit = EaS_dmg * 2.50

        FlS_dmg = (SP * 0.195) + (SP * 0.195) * versCons
        FlS_crit = FlS_dmg * 2.50

        FlS_tick = (SP * 0.058) + (SP * 0.058) * versCons
        FlS_tick_crit = FlS_tick * 2.50

        FlS_applied = False
        FlS_timer = 0

        LB1_applied = False
        LB1_timer = 0
        LB2_applied = False
        LB2_timer = 0

        IF_applied = False
        IF_timer = 0

        echS_timer = 0

        Asc_timer = 0
        Asc_applied = False

        EaS_applied = False
        EQ_applied = False

        maelstrom = 0



        while time > 0:
            if IF_timer >= 30:
                IF_timer == 0
            if echS_timer >= 30:
                echS_timer = 0
                
            if LB1_timer >= 8:
                LB1_timer = 0
            if LB2_timer >= 8:
                LB2_timer = 0
            if Asc_timer >= 180:
                Asc_timer = 0
            if FlS_timer >= 18:
                FlS_timer = 0
            if  FlS_timer<=18 and FlS_applied == False:
                FlS_applied = True
                time = time - GCD
                FlS_timer = FlS_timer + GCD
                dmg_roll = random.randint(1,100)
                if dmg_roll > 100 - (100 * critCons):
                    tot_dmg = tot_dmg + (FlS_dmg * 2.50)
                    tot_dmg = tot_dmg + (FlS_tick * 18)
                elif dmg_roll < 100 - (100 * critCons):
                    tot_dmg = tot_dmg + FlS_dmg + (FlS_tick * 18)
                if LB1_timer > 0:
                    LB1_timer = LB1_timer + GCD
                if LB2_timer > 0:
                    LB2_timer = LB2_timer + GCD
                if echS_timer > 0 :
                    echS_timer = echS_timer + GCD
                if Asc_timer > 0:
                    Asc_timer = Asc_timer + GCD
                if IF_timer > 0:
                    IF_timer = IF_timer + GCD
            
           
            elif FlS_timer >= 18:
                FlS_applied = False
                FlS_timer = 0
                
            if Asc_timer == 0 and echS_timer == 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                echS_timer = echS_timer + 15
                if Asc_applied == True:
                    tot_dmg = tot_dmg + echS_dmg + LB_crit
                    for i in range(1-9):
                        tot_dmg = tot_dmg + (LB_crit)
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time -15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                    
            elif Asc_timer == 0 and echS_timer > 0 and FlS_applied == True:
                Asc_applied = True
                FlS_timer = 0
                LB1_timer = 0
                LB2_timer = 0
                if Asc_applied == True:
                    for i in range(1-9):
                        tot_dmg = tot_dmg + LB_crit
                        maelstrom = maelstrom + 10
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                    time = time - 15
                    Asc_applied = False
                    FlS_timer = FlS_timer + 15
                    Asc_timer = Asc_timer + 15
                    if IF_timer > 0:
                        IF_timer = IF_timer + 15
                        
            
                    
                    
                
                
          

                
                    
                    
            if LB1_timer == 0 or LB2_timer == 0:
                if LB1_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB1_timer = LB1_timer + GCD 
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer +GCD+GCD+cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB2_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 5)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*5)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_tiemr = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast + GCD
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0

                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer= 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                      


                
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + GCD + cast
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer =0
                        elif maelstrom + 20 >= 60 and LB1_timer == 0 and LB2_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                                
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer  = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast * 2) + (GCD * 4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB1_timer = LB1_timer + (cast*2) + (GCD*3)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                                if LB2_timer >= 8:
                                    LB2_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB1_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB2_timer > 0:
                                LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            
                    
                    
                  

                elif LB2_timer == 0:
                    if echS_timer == 0:
                        if maelstrom >= 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + echS_dmg
                            maelstrom = maelstrom - 60
                            time = time - (GCD*2) - cast
                            FlS_timer = FlS_timer + (GCD*2) + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            echS_timer = echS_timer + (GCD*2) + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            Asc_timer = Asc_timer + (GCD*2) + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + (GCD*2) + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                    
                        elif maelstrom + 10>= 60 or maelstrom + 20 >= 60 and maelstrom < 60:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + echS_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom + 20
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            time = time - GCD - cast - GCD  
                            echS_timer = echS_timer + GCD + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer +GCD + cast + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer +GCD+GCD+cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            maelstrom = maelstrom - 60
                                

                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 45 >= 60 and LB1_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            maelstrom = maelstrom + 45
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 3) + (FrS_dmg * 2.5) + (FrS_dmg * 3) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 3) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) + echS_dmg
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 5) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 6) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 5)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*6) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 5) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 5) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        
                        elif IF_timer == 0 and maelstrom < 60:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + (LB_crit * 2) + echS_dmg
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + (LB_crit * 2) +echS_dmg
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*5) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*4)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*5) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*5)
                            if LB1_timer >= 8:
                                LB1_timer =0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*4)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif IF_timer > 0 and LB2_timer > 0 and maelstrom < 60:
                            tot_dmg = tot_dmg + (LB_crit *2) + echS_dmg
                            time = time- cast - GCD
                            maelstrom = maelstrom + 20
                            echS_timer = echS_timer + cast + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast + GCD
                            if Fls_timer >= 18:
                                FlS_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0       
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast +GCD
                                if IF_timer >=30:
                                     IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        else:
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LiB_dmg
                            time = time - cast
                            LB1_timer = LB1_timer + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            LB2_timer = LB2_timer + cast
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            maelstrom = maelstrom + 8
                    
                            if IF_timer > 0:
                                IF_timer = IF_timer + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if FlS_timer > 0:
                                FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                            if Asc_timer >= 180:
                                Asc_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                        
                            
                    elif echS_timer > 0:
                        if maelstrom + 10 >= 60 and LB2_timer == 0:
                            maelstrom = maelstrom + 10
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + LB_crit + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20)
                            maelstrom = maelstrom - 60
                            time = time - GCD - cast
                            LB2_timer = LB2_timer + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            echS_timer = echS_timer + GCD + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + GCD + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if IF_timer > 0:
                                IF_timer = IF_timer + GCD + cast
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + GCD + cast
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + GCD + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif maelstrom + 20 >= 60 and LB2_timer == 0 and LB1_timer == 0:
                            maelstrom = maelstrom + 20
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + (LB_crit * 2) + ((EaS_dmg + EaS_dmg * 0.20) * 2.50)
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + EaS_dmg + (EaS_dmg * 0.20) + (LB_crit * 2)
                            time = time - (cast*2) - GCD
                            LB2_timer = LB2_timer + cast + GCD
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (cast*2) + GCD
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + (cast*2) + GCD
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            maelstrom = maelstrom - 60
                            if IF_timer > 0:
                                IF_timer = IF_timer + (cast*2) + GCD
                                if IF_timer >= 30:
                                    IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (cast*2) + GCD
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                        elif IF_timer == 0 and maelstrom < 60 and maelstrom + 35 >= 60 and LB1_timer == 0:
                            maelstrom = maelstrom + 35
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg *3.0)
                            EaS_dmg = EaS_dmg + (EaS_dmg * 0.20)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + ((EaS_dmg + EaS_dmg * 0.20) * 2.50) + (LB_crit * 2) + (FrS_dmg * 2.5) + (FrS_dmg * 3) 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (LB_crit * 2) + EaS_dmg + (EaS_dmg * 0.20) + (FrS_dmg * 4) 
                            IF_dmg = IF_dmg - (IF_dmg + 0.20)
                            FrS_dmg = FrS_dmg/3
                            EaS_dmg = EaS_dmg - (EaS_dmg * 0.20)
                            time = time  - (GCD * 4) - (cast * 3)
                            FlS_timer = FlS_timer + (GCD * 5) + (cast * 3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast * 2) + (GCD * 4)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            LB1_timer = LB1_timer + GCD
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            echS_timer = echS_timer + (GCD*5) + (cast*3)
                            if echS_timer >= 30:
                                echS_timer = 0
                            IF_timer = IF_timer + (GCD * 4) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD * 4) + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            maelstrom = maelstrom - 60
                        elif IF_timer == 0:
                            IF_dmg = IF_dmg + (IF_dmg * 0.20)
                            FrS_dmg = (FrS_dmg * 3.0)
                            dmg_roll = random.randint(1,100)
                            if dmg_roll > 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 2.5) + (FrS_dmg * 3) + LB_crit 
                            elif dmg_roll < 100 - (100 * critCons):
                                tot_dmg = tot_dmg + IF_dmg + (FrS_dmg * 4) + LB_crit  
                            FrS_dmg = FrS_dmg/3.0
                            IF_dmg = IF_dmg - (IF_dmg * 0.20)
                            maelstrom = maelstrom + 45
                            time = time - cast - (GCD*4) - cast
                            FlS_timer = FlS_timer + (cast*2) + (GCD*3)
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            LB2_timer = LB2_timer + (cast*2) + (GCD*3)
                            if LB2_timer >= 8:
                                LB2_timer = 0
                            IF_timer = IF_timer + (GCD*3) + cast
                            if IF_timer >= 30:
                                IF_timer = 0
                            echS_timer = echS_timer + (GCD*4) + (cast*2)
                            if echS_timer >= 30:
                                echS_timer = 0
                            
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + (GCD*4) + (cast*2)
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + (cast*2) + (GCD*4)
                            if LB1_timer >= 8:
                                LB1_timer = 0
                            if echS_timer > 0:
                                echS_timer = echS_timer + (cast*2) + (GCD*3)
                                if echS_timer >= 30:
                                    echS_timer = 0
                        elif LB2_timer == 0 and FlS_timer <= 18:
                            tot_dmg = tot_dmg + LB_crit
                            
                            time = time - cast
                            echS_timer = echS_timer + cast
                            if echS_timer >= 30:
                                echS_timer = 0
                            FlS_timer = FlS_timer + cast
                            if FlS_timer >= 18:
                                FlS_timer = 0
                            if Asc_timer > 0:
                                Asc_timer = Asc_timer + cast
                                if Asc_timer >= 180:
                                    Asc_timer = 0
                            if LB1_timer > 0:
                                LB1_timer = LB1_timer + cast
                                
                            if LB1_timer >= 8:
                                LB1_timer = 0

                
            else:
                    dmg_roll = random.randint(1,100)
                    if dmg_roll > 100 - (100 * critCons):
                        tot_dmg = tot_dmg + (LiB_dmg * 2.5)
                    elif dmg_roll < 100 - (100 * critCons):
                        tot_dmg = tot_dmg + LiB_dmg
                    time = time - cast
                    LB1_timer = LB1_timer + cast
                    if LB1_timer >= 8:
                        LB1_timer = 0
                    LB2_timer = LB2_timer + cast
                    if LB2_timer >= 8:
                        LB2_timer = 0
                    maelstrom = maelstrom + 8
                    
                    if IF_timer > 0:
                        IF_timer = IF_timer + cast
                        if IF_timer >= 30:
                            IF_timer = 0
                    if FlS_timer > 0:
                        FlS_timer = FlS_timer + cast
                        if FlS_timer >= 18:
                            FlS_timer = 0
                    if Asc_timer > 0:
                        Asc_timer = Asc_timer + cast
                        if Asc_timer >= 180:
                            Asc_timer = 0
                    if echS_timer > 0:
                        echS_timer = echS_timer + cast
                    if echS_timer >= 30:
                        echS_timer = 0


        tot_dmg = tot_dmg + ((fight_time/34) * LB_crit)
        tot_dmg = tot_dmg + ((tot_dmg * mastCons) * 0.85)

       


        DPS_int = tot_dmg/fight_time
        "print(DPS_int)"
        DPS_list.append(DPS_int)
        avgINTL.append(DPS_int)

        
        statPercents[0] = intCons 
        SP = intCons
        "print(SP)"


        FlS_applied = False
        FlS_timer = 0

        LB1_applied = False
        LB1_timer = 0
        LB2_applied = False
        LB2_timer = 0

        IF_applied = False
        IF_timer = 0

        echS_timer = 0

        Asc_timer = 0
        Asc_applied = False

        EaS_applied = False
        EQ_applied = False

        maelstrom = 0


        """LiB_dmg = (SP * 0.95) + (SP * 0.95) * statPercents[3] 
        LiB_crit = LiB_dmg * 2.50



        LB_dmg = (SP * 1.08) + (SP * 1.08) * statPercents[3]
        LB_crit = LB_dmg * 2.50


        IF_dmg = (SP * 0.825) + (SP * 0.825) * statPercents[3]
        IF_crit = IF_dmg * 2.50

        CL_dmg = ((SP * 0.47) + (SP * 0.47) * statPercents[3]) * numTrgts
        CL_crit = CL_dmg * 2.50

        FrS_dmg = (SP * 0.45) + (SP * 0.45) * statPercents[3]
        FrS_crit = FrS_dmg * 2.50

        EQ_dmg = ((SP * 0.23) + (SP * 0.23) * statPercents[3]) * numTrgts
        EQ_crit = EQ_dmg * 2.50

        echS_dmg = (SP * 0.65) + (SP * 0.65) * statPercents[3]
        echS_crit = echS_dmg * 2.50

        EaS_dmg = (SP * 2.10) + (SP * 2.10) * statPercents[3]
        EaS_crit = EaS_dmg * 2.50

        FlS_dmg = (SP * 0.195) + (SP * 0.195) * statPercents[3]
        FlS_crit = FlS_dmg * 2.50

        FlS_tick = (SP * 0.058) + (SP * 0.058) * statPercents[3]
        FlS_tick_crit = FlS_tick * 2.50"""

        



        "print(DPS_list)"
        
        DPS_list = []
        tot_dmg = 0
        time = fight_time
        
    if gearCompared == False:
        gear_compare_user = str(input("Would you like to compare your set of gear with another set of gear? (type 'C') \n Take a look at stat weights? (type 'W') \n Or nothing? (type anything)"))
        
        
        
    if gear_compare_user == "C":
        simCollector = True
        gear = True
        gearCompared = True
        initDPS = 0
        initMAST = 0
        initVERS = 0
        initCRIT = 0
        initHAST = 0
        initINT = 0
    
        for sim in avgDPS:
            initDPS = initDPS + sim
        initDPS = initDPS/sim_count
        "print(initDPS)"
        for sim in avgMAST:
            initMAST = initMAST + sim
        initMAST = initMAST/sim_count
        "print(initMAST)"
        for sim in avgVERS:
            initVERS = initVERS + sim
        initVERS = initVERS/sim_count
        "print(initVERS)"
        for sim in avgCRIT:
            initCRIT = initCRIT + sim
        initCRIT = initCRIT/sim_count
        "print(initCRIT)"
        for sim in avgHAST:
            initHAST = initHAST + sim
        initHAST = initHAST/sim_count
        "print(initHAST)"
        for sim in avgINTL:
            initINT = initINT + sim
        initINT = initINT/sim_count
        "print(initINT)"

        avgTOTAL.append(initDPS)
        avgTOTAL.append(initHAST)
        avgTOTAL.append(initCRIT)
        avgTOTAL.append(initVERS)
        avgTOTAL.append(initMAST)
        avgTOTAL.append(initINT)
        "print(avgTOTAL)"
        DPSCollector.append(avgTOTAL)
        ovrSTATS.append(statCollector)
        print("You did",initDPS,"DPS this run")
        

    elif gear_compare_user == "W":
        simCollector = True
        gear = True
        gearCompared = True
        initDPS = 0
        initMAST = 0
        initVERS = 0
        initCRIT = 0
        initHAST = 0
        initINT = 0
    
        for sim in avgDPS:
            initDPS = initDPS + sim
        initDPS = initDPS/sim_count
        "print(initDPS)"
        for sim in avgMAST:
            initMAST = initMAST + sim
        initMAST = initMAST/sim_count
        "print(initMAST)"
        for sim in avgVERS:
            initVERS = initVERS + sim
        initVERS = initVERS/sim_count
        "print(initVERS)"
        for sim in avgCRIT:
            initCRIT = initCRIT + sim
        initCRIT = initCRIT/sim_count
        "print(initCRIT)"
        for sim in avgHAST:
            initHAST = initHAST + sim
        initHAST = initHAST/sim_count
        "print(initHAST)"
        for sim in avgINTL:
            initINT = initINT + sim
        initINT = initINT/sim_count
        "print(initINT)"
        print("Your base DPS for this run was",initDPS)
        print("Your Haste run had",initHAST,"DPS")
        print("Your Crit run had",initCRIT,"DPS")
        print("Your Versatility run had",initVERS,"DPS")
        print("Your Mastery run had",initMAST,"DPS")
        print("Your Intellect run had",initINT,"DPS")
        mastWeight = (initMAST - initDPS)/65.2
        versWeight = (initVERS - initDPS)/140
        intWeight = (initINT - initDPS)/(intCons * 0.035) 
        critWeight = (initCRIT - initDPS)/121
        hastWeight = (initHAST - initDPS)/115.5
        print("Your Intellect weight is",intWeight)
        print("Your Haste weight is",hastWeight)
        print("Your Crit weight is",critWeight)
        print("Your Versatility weight is",versWeight)
        print("Your Mastery weight is",mastWeight)
        simCollector = False
        
    else:
       
        initDPS = 0
        initMAST = 0
        initVERS = 0
        initCRIT = 0
        initHAST = 0
        initINT = 0
    
        for sim in avgDPS:
            initDPS = initDPS + sim
        initDPS = initDPS/sim_count
        "print(initDPS)"
        for sim in avgMAST:
            initMAST = initMAST + sim
        initMAST = initMAST/sim_count
        "print(initMAST)"
        for sim in avgVERS:
            initVERS = initVERS + sim
        initVERS = initVERS/sim_count
        "print(initVERS)"
        for sim in avgCRIT:
            initCRIT = initCRIT + sim
        initCRIT = initCRIT/sim_count
        "print(initCRIT)"
        for sim in avgHAST:
            initHAST = initHAST + sim
        initHAST = initHAST/sim_count
        "print(initHAST)"
        for sim in avgINTL:
            initINT = initINT + sim
        initINT = initINT/sim_count
        "print(initINT)"

        avgTOTAL.append(initDPS)
        avgTOTAL.append(initHAST)
        avgTOTAL.append(initCRIT)
        avgTOTAL.append(initVERS)
        avgTOTAL.append(initMAST)
        avgTOTAL.append(initINT)
        "print(avgTOTAL)"
        """print("Have a nice day in Azeroth")"""
        print("Your base DPS was",initDPS)
        
        simCollector = False
        gear = False


    if gear == True and len(DPSCollector) > 1:
        ovrDPS = DPSCollector[1][0] - DPSCollector[0][0]
        ovrHAS = DPSCollector[1][1] - DPSCollector[0][1]
        ovrCRIT = DPSCollector[1][2] - DPSCollector[0][2]
        ovrVERS = DPSCollector[1][3] - DPSCollector[0][3]
        ovrMAST = DPSCollector[1][4] - DPSCollector[0][4]
        ovrINT = DPSCollector[1][5] - DPSCollector[0][5]
        

        IntellectDiff = statCollector[1][0] - statCollector[0][0]
        print("The difference in Intellect between the two sets is" + " ",IntellectDiff,"points")
        HasteDiff = (statCollector[1][1] - statCollector[0][1]) * 100
        print("The difference in Haste between the two sets is" + " ",HasteDiff,"percent")
        CritDiff = (statCollector[1][2] - statCollector[0][2]) * 100
        print("The difference in Crit between the two sets is" + " ",CritDiff,"percent")
        VersDiff = (statCollector[1][3] - statCollector[0][3]) * 100
        print("The difference in Versatiliy between the two sets is" +" ",VersDiff,"percent")
        MastDiff = (statCollector[1][4] - statCollector[0][4]) * 100
        print("The difference in Mastery between the two sets is" + " ",MastDiff,"percent")
        
        print("The difference in base DPS is" + " ",ovrDPS)
        simCollector = False
        
        
        
        
              

    






                
          
            
        

    



     



