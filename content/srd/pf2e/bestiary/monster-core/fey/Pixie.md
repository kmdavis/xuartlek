---
noteType: pf2eMonster
aliases: "Pixie"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/sprite
  - pf2e/creature/trait/small
statblock: inline
name: "Pixie"
level: 4
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3212"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Pixie"
level: "Creature 4"
size: "Small"
trait_01: "Fey"
trait_02: "Sprite"
modifier: 12
perception:
  - name: "Perception"
    desc: "+12; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +11, [[srd/pf2e/compendium/rules-elements/skills/Nature|Nature]] +10, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +11"
abilityMods: [-1, 5, 1, 3, 2, 3]
abilities_top:
  - name: "Items"
    desc: "Longbow (60 arrows), Shortsword"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +8; __Ref__: +14; __Will__: +12 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 40
health:
  - name: "HP"
    desc: "40; __Weaknesses__ cold iron 5"
speed: "15 feet, fly 45 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d6+4 piercing"
  - name: "Ranged"
    desc: "⬻ longbow +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Deadly|deadly d10]], range increment 100 feet, reload 0, [[srd/pf2e/compendium/rules-elements/traits/player-core/Volley|volley 20 feet]]) __Damage__ 1d8+4 piercing"
abilities_bot:
  - name: "Sprinkle Pixie Dust"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Manipulate|Manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|Primal]]) The pixie sprinkles pixie dust onto one of their arrows. If the pixie hits a creature with that arrow before the pixie's next turn, the arrow inflicts one of the following special effects of the pixie's choice instead of dealing damage. Each effect depends on the target's DC 21 Will save. On a critical hit, the target gets a result one degree worse than it rolled. Charm ([[srd/pf2e/compendium/rules-elements/traits/player-core/Emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) The arrow has the effect of a charm spell, except the target doesn't gain a bonus to its save if the only hostile act was the pixie firing its bow, and the pixie can choose to direct the target's adoration toward another creature rather than itself.Memory Loss ([[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) On a failed Will save, the target loses the last 5 minutes of its memory.Sleep ([[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sleep|sleep]]) The target suffers the effects of a 3rd- rank sleep spell.Subdual ([[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|nonlethal]]) The target takes 4d6 mental damage, depending on its basic Will save. Variant Pixie Arrows Pixies can enchant their arrows with a wide variety of effects, though nearly all such enchantments are designed to charm or bewilder, never maim. Some arrows may emulate the effects of spells such as [[srd/pf2e/compendium/spells/rank-4/Confusion|_confusion_]], [[srd/pf2e/compendium/spells/rank-1/Fear|_fear_]], [[srd/pf2e/compendium/spells/rank-2/Laughing Fit|_laughing fit_]], and even [[srd/pf2e/compendium/spells/rank-4/Suggestion|_suggestion_]]."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Shield|Shield]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Entangling Flora|Entangling Flora]], [[srd/pf2e/compendium/spells/rank-2/Revealing Light|Revealing Light]] - __3rd__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]] - __4th__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (at will; self only)"
sourcebook: "_Monster Core_, page 323."
```

```encounter-table
name: Pixie
creatures:
  - 1: Pixie
```
