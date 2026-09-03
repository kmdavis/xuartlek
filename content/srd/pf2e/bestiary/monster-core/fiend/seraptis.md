---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Seraptis"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/demon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Seraptis"
level: 15
source: "Monster Core"
aon_id: "creature-2899"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2899"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Seraptis"
level: "Creature 15"
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, [[srd/pf2e/compendium/spells/rank-6/truesight|_truesight_]]"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; telepathy 100 feet, [[srd/pf2e/compendium/spells/rank-5/truespeech|_truespeech_]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +30, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +31, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +29, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +27, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +28"
abilityMods: [8, 7, 6, 3, 4, 6]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/runes/wounding|wounding]] [[srd/pf2e/compendium/equipment/weapons/sword/scimitar|scimitar]]_ (2)"
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +27; __Ref__: +28; __Will__: +25 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 340
health:
  - name: "HP"
    desc: "340; __Weaknesses__ cold iron 15, [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 15"
abilities_mid:
  - name: "Blood Healing"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]]) 30 feet. Whenever a humanoid within the aura takes bleed damage, the blood flows through the air to the seraptis's mouths and the seraptis heals by the same amount."
  - name: "Recovery Vulnerability"
    desc: "When a creature within the seraptis's blood healing aura recovers from [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent damage]], the seraptis takes 3d6 mental damage."
speed: "40 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _wounding scimitar_ +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d6+16 slashing plus 2d6 mental and 1d6 persistent bleed"
  - name: "Melee"
    desc: "⬻ claw +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d4+16 slashing plus 2d6 mental and Grab"
  - name: "Ranged"
    desc: "⬻ caustic blood +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 7d6 acid"
abilities_bot:
  - name: "Bloody Dance"
    desc: "⬺ The seraptis makes a Strike with up to four arms, each against a different target and using a claw or scimitar as appropriate. These attacks count toward the seraptis's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks. The seraptis can use Grab following this activity, separately attempting to [[srd/pf2e/compendium/rules-elements/actions/player-core#Grapple|Grapple]] each creature hit by a claw."
  - name: "Gnawing Arms"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]])"
  - name: "Requirements"
    desc: "The seraptis has at least one creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]"
  - name: "Effects"
    desc: "The seraptis's arm mouths gnaw on those creatures, dealing each of them 2d6+8 piercing damage with a DC 37 basic Fortitude save. Creatures that fail the save also take 2d6 persistent bleed damage."
  - name: "Isolating Words"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|Linguistic]]) The seraptis telepathically explains a plausible secret to a creature within 30 feet. That creature must succeed at a DC 37 Will save or be mentally cut off from those around them for 1 minute (or permanently on a critical failure). The affected creature treats no one as an ally and any speech they hear is warped, encouraging conflict, and negating any [[srd/pf2e/compendium/rules-elements/traits/player-core/linguistic|linguistic]] ability from creatures that aren't [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]. Regardless of the results of the saving throw, the creature is immune to Isolating Words for 24 hours."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 35 - __3rd__ [[srd/pf2e/compendium/spells/rank-1/illusory-disguise|Illusory Disguise]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __5th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __8th__ [[srd/pf2e/compendium/spells/rank-6/dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-6/phantasmal-calamity|Phantasmal Calamity]], [[srd/pf2e/compendium/spells/rank-5/wave-of-despair|Wave of Despair]] - __Constant (8th)__ [[srd/pf2e/compendium/spells/rank-6/truesight|Truesight]], [[srd/pf2e/compendium/spells/rank-5/truespeech|Truespeech]]"
  - name: "Rituals"
    desc: "DC 36 - __1st__ [[srd/pf2e/compendium/spells/rituals/demonic-pact|Demonic Pact]]"
sourcebook: "_Monster Core_, page 80."
```

```encounter-table
name: Seraptis
creatures:
  - 1: Seraptis
```
