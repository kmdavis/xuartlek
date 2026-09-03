---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Azuretzi"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/protean
  - pf2e/creature/trait/small
statblock: inline
name: "Azuretzi"
level: 5
source: "Monster Core"
aon_id: "creature-3145"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3145"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Azuretzi"
level: "Creature 5"
size: "Small"
trait_01: "Monitor"
trait_02: "Protean"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision, entropy sense (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Protean"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +11, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +11, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +13, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +13, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +11, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +13"
abilityMods: [2, 4, 4, 4, 2, 4]
abilities_top:
  - name: "Entropy Sense"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/prediction|prediction]]) A protean can anticipate the most likely presence of a creature through a supernatural insight into chaotic probabilities and chance. This grants them the ability to sense creatures within the listed range. [[srd/pf2e/compendium/spells/rank-3/veil-of-privacy|_Veil of privacy_]] prevents a creature from being detected via entropy sense automatically (without a counteract check)."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +15; __Will__: +11 +1 status to all saves vs. magic"
hp: 65
health:
  - name: "HP"
    desc: "65 (fast healing 2); __Resistances__ precision 5, protean anatomy 8"
abilities_mid:
  - name: "Protean Anatomy"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]) A protean's vital organs shift and change shape and position constantly. Immediately after the protean takes acid, electricity, or sonic damage, they gain the listed amount of resistance to that damage type. This lasts for 1 hour or until the next time the protean takes damage of one of the other types (in which case their resistance changes to match that type), whichever comes first. The protean is immune to [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|polymorph]] effects unless they're a willing target. If [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] or [[srd/pf2e/compendium/rules-elements/conditions#Deafened|deafened]], the protean automatically recovers at the end of their next turn as new sensory organs grow to replace the compromised ones."
  - name: "Spell Pilfer"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature with an active spell effect within 30 feet of the azuretzi fails to resist another azuretzi's Mocking Touch"
  - name: "Effect"
    desc: "The azuretzi attempts a [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] check to counteract one spell affecting the target creature. On a success, the azuretzi transfers the spell effect to themself, keeping the same remaining duration. The target then becomes temporarily immune to Spell Pilfer for 24 hours."
speed: "25 feet, fly 25 feet, swim 25 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d10+5 piercing"
  - name: "Melee"
    desc: "⬻ claw +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 2d8+5 slashing"
  - name: "Melee"
    desc: "⬻ tail +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d12+5 bludgeoning plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d12+5 bludgeoning, DC 21"
  - name: "Mimic Form"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]]) As Change Shape, but an azuretzi can assume the form of a Medium or smaller creature. They can mimic a specific creature they can see, but they must succeed at a DC 25 Perception check or the attempt is disrupted. The azuretzi can transform into the same creature again without a check but can retain the details of only one specific appearance at a time. The azuretzi can Dismiss the effect as a free action to return to their natural form."
  - name: "Mocking Touch"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Requirements"
    desc: "The azuretzi is not currently using Mocking Touch on a spell"
  - name: "Effect"
    desc: "The azuretzi mocks a creature's magical ability with a touch. The azuretzi attempts a [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] check against the target's Will DC."
  - name: "Critical Success"
    desc: "The azuretzi learns all spells of 3rd rank or lower the target has available to cast and chooses one. The azuretzi gains that spell as a mock divine innate spell and can cast it once as an innate divine spell using their own DC and spell attack modifier. The spell is lost if unused after 24 hours. The creature can't cast the mock spell until the azuretzi casts it first or the 24 hour period passes, whichever comes first."
  - name: "Success"
    desc: "As critical success, but the mock spell is lost after 1 hour, and the creature touched can cast the spell normally."
  - name: "Failure"
    desc: "As critical success, but the mock spell is lost at the end of the azuretzi's next turn, and the creature touched can cast the spell normally."
  - name: "Critical Failure"
    desc: "Mocking Touch has no effect."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 22 - __2nd__ [[srd/pf2e/compendium/spells/rank-2/laughing-fit|Laughing Fit]] - __3rd__ [[srd/pf2e/compendium/spells/rank-3/crisis-of-faith|Crisis of Faith]], [[srd/pf2e/compendium/spells/rank-2/dispel-magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-2/shatter|Shatter]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __Constant (4th)__ [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]]"
sourcebook: "_Monster Core_, page 271."
```

```encounter-table
name: Azuretzi
creatures:
  - 1: Azuretzi
```
