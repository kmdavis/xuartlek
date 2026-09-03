---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ninkonda"
tags:
  - pf2e/creature/level/17
  - pf2e/creature/trait/angel
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Ninkonda"
level: 17
source: "Monster Core 2"
aon_id: "creature-4031"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4031"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ninkonda"
level: "Creature 17"
size: "Large"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: "Uncommon"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +27, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +34, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +34, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +30, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +28, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +26"
abilityMods: [9, 4, 7, 3, 6, 7]
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +30; __Ref__: +27; __Will__: +33"
hp: 350
health:
  - name: "HP"
    desc: "350; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]] 15"
abilities_mid:
  - name: "Aura of Reflection"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 60 feet. The ninkonda's mirror reflects the weaknesses in creatures' souls. A creature that enters or starts its turn in the aura must succeed at a DC 36 Will save or be [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] and take a –2 penalty to Will saves against the ninkonda's abilities for 1 round."
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Reflect Spell"
    desc: "⬲"
  - name: "Trigger"
    desc: "The ninkonda is targeted by a ranged spell attack"
  - name: "Effect"
    desc: "The ninkonda attempts to reflect the spell with the mirror in their armor. They gain a +4 circumstance bonus to AC against the triggering attack. If the attack misses, the spell is reflected back at the caster, who must roll a second ranged spell attack against their own AC to determine if the spell hits them instead."
speed: "30 feet, fly 45 feet"
attacks:
  - name: "Melee"
    desc: "⬻ nailed fist +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile P]]) __Damage__ 2d6+17 bludgeoning plus 2d8 piercing"
  - name: "Ranged"
    desc: "⬻ nail blast +34 ([[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range 60 feet) __Damage__ 3d8+8 piercing plus 2d8 persistent bleed"
abilities_bot:
  - name: "Nail Barrage"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]]) The ninkonda sprays a mass of nails that deal 14d8 piercing damage in a 20-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] with a DC 38 basic Reflex save. They can't use Nail Barrage again for 1d4 rounds."
  - name: "Soul Reflection"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|Holy]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) The ninkonda aims the mirror in their armor at a creature [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] by their aura of reflection to force the creature to gaze upon its past sins. The creature must succeed at a DC 38 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]] for 1 round as it reflects upon its actions (or 1 minute on a critical failure, as the creature's actions continue to weigh on it). A [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] creature or a morally upstanding creature (as determined by the GM) uses the outcome that is one degree of success better than it rolled on its save. A creature that fails its save is then temporarily immune to Soul Reflection for 1 minute. Seeking Redemption Ninkondas have a particularly unique origin among angels. While the occasional ninkonda is born from the soul of a righteous mortal who sought to continue their work of redeeming others in the afterlife, most stem from the ranks of the less scrupulous. After centuries or millennia of perseverance, souls seeking true redemption earn the ability to join the celestial ranks of angels, usually as cassisians or other lowly beings. As they rise through the celestial ranks, they gravitate toward the role of ninkondas in hopes of helping others. In a way, ninkondas are self-perpetuating. Given enough time, they could amass countless angels within their ranks thanks to their own efforts."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30 - __Cantrips (9th)__ [[srd/pf2e/compendium/spells/cantrips/divine-lance|Divine Lance]], [[srd/pf2e/compendium/spells/cantrips/light|Light]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/ring-of-truth|Ring of Truth]] (at will) - __7th__ [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|Interplanar Teleport]] (self only) - __8th__ [[srd/pf2e/compendium/spells/rank-8/pinpoint|Pinpoint]] - __Constant (6th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]], [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 38 - __1st__ Angelic Messenger - __4th__ Atone"
sourcebook: "_Monster Core 2_, page 29."
```

```encounter-table
name: Ninkonda
creatures:
  - 1: Ninkonda
```
