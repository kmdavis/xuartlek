---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Pleroma"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/aeon
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/large
statblock: inline
name: "Pleroma"
level: 20
source: "Monster Core"
aon_id: "creature-2811"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2811"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pleroma"
level: "Creature 20"
size: "Large"
trait_01: "Aeon"
trait_02: "Monitor"
modifier: 37
perception:
  - name: "Perception"
    desc: "Perception +37; darkvision, lifesense 120 feet, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]; envisioning"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +33, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +38, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +34, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +34, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +38, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +39, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +35"
abilityMods: [6, 7, 6, 8, 9, 6]
abilities_top:
  - name: "Envisioning"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 100 feet. A pleroma can communicate mentally with any creatures in the aura using wordless psychic projections. They don't need to share a language, though the aeon's meaning to non-aeons can be vague and is often mysterious. An aeon can use this ability to communicate flawlessly with any other aeon on the same plane as itself."
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +32; __Ref__: +31; __Will__: +37 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 335
health:
  - name: "HP"
    desc: "335 , regeneration 20 (deactivated by [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]]); __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Weaknesses__ spirit 20"
abilities_mid:
  - name: "Reality Twist"
    desc: "⬲"
  - name: "Trigger"
    desc: "The pleroma critically fails a saving throw"
  - name: "Effect"
    desc: "The critical failure becomes a normal failure."
speed: "fly 40 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ touch of creation +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|Vitality]]) __Damage__ 5d8+16 vitality"
  - name: "Melee"
    desc: "⬻ touch of destruction +36 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|Void]]) __Damage__ 5d8+16 void"
abilities_bot:
  - name: "Generate Sphere"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) The pleroma manifests a 2-foot-diameter sphere of energy—either a white sphere of creation that hovers above their left hand or a black sphere of oblivion above their right. This action has the [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] trait for a sphere of creation or the [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]] trait for a sphere of oblivion. A sphere vanishes after 1 minute, when it is more than 300 feet from the pleroma, or when the pleroma Generates a Sphere of that type again. A sphere of oblivion winks out of existence when it vanishes, but a sphere of creation explodes in blinding light—each creature in a 30-foot emanation must succeed at a DC 43 Fortitude save or be permanently [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]]. This is a [[srd/pf2e/compendium/rules-elements/traits/player-core/light|light]] effect."
  - name: "Propel Sphere"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Requirements"
    desc: "The pleroma has a sphere of creation or sphere of oblivion active"
  - name: "Effect"
    desc: "The pleroma makes one of its spheres fly 10 feet in any direction, ignoring difficult terrain and greater difficult terrain. A sphere of creation creates new matter in its path, which the pleroma can have manifest as normal terrain, difficult terrain, greater difficult terrain, or a cube of solid mater (such as clay, wood, or stone). A sphere of oblivion destroys unattended objects it touches, though larger objects are destroyed at a rate of one 10-foot cube per round of contact. The sphere can enter the space of a creature; when it does, the creature takes 20d6 damage with a DC 43 Fortitude save. This is an [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]] effect."
  - name: "Success"
    desc: "The creature takes no damage and is pushed out of the sphere to the nearest open space of the GM's choice."
  - name: "Failure"
    desc: "The creature takes full damage; this is vitality damage for a sphere of creation or void damage for a sphere of oblivion, but it can damage any type of creature regardless of its normal immunities. The creature is then pushed out of the sphere as on a success. A creature reduced to 0 HP is slain instead of being pushed out, either merged with new matter for a sphere of creation or completely destroyed for a void of oblivion; the creature can be restored only via a [[srd/pf2e/compendium/spells/rituals/wish|_wish_]] ritual or similarly powerful effect. This is a [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effect."
  - name: "Critical Failure"
    desc: "As failure, but the creature takes double damage."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 47, attack +39 - __Cantrips (10th)__ [[srd/pf2e/compendium/spells/cantrips/vitality-lash|Vitality Lash]], [[srd/pf2e/compendium/spells/cantrips/void-warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/create-water|Create Water]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/shape-wood|Shape Wood]] (at will) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/hypercognition|Hypercognition]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-2/create-food|Create Food]] (at will), [[srd/pf2e/compendium/spells/rank-4/shape-stone|Shape Stone]] (at will), [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]] - __5th__ [[srd/pf2e/compendium/spells/rank-4/creation|Creation]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]], [[srd/pf2e/compendium/spells/rank-7/retrocognition|Retrocognition]] - __8th__ [[srd/pf2e/compendium/spells/rank-6/disintegrate|Disintegrate]] (×2), [[srd/pf2e/compendium/spells/rank-8/unrelenting-observation|Unrelenting Observation]] - __9th__ [[srd/pf2e/compendium/spells/rank-5/banishment|Banishment]], [[srd/pf2e/compendium/spells/rank-6/blessed-boundary|Blessed Boundary]], [[srd/pf2e/compendium/spells/rank-9/detonate-magic|Detonate Magic]], [[srd/pf2e/compendium/spells/rank-9/overwhelming-presence|Overwhelming Presence]] - __10th__ [[srd/pf2e/compendium/spells/rank-10/manifestation|Manifestation]] - __Constant (8th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]]"
sourcebook: "_Monster Core_, page 10."
```

```encounter-table
name: Pleroma
creatures:
  - 1: Pleroma
```
