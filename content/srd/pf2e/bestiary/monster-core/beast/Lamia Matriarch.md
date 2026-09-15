---
noteType: pf2eMonster
aliases: "Lamia Matriarch"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Lamia Matriarch"
level: 8
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3078"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lamia Matriarch"
level: "Creature 8"
size: "Large"
trait_01: "Beast"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "+15; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +18, Cult Lore +15, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +20, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +20, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +18, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +17, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +16, [[srd/pf2e/compendium/rules-elements/skills/Survival|Survival]] +13"
abilityMods: [6, 4, 3, 3, 3, 6]
abilities_top:
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/weapons/sword/Scimitar|scimitar]]_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +13; __Ref__: +18; __Will__: +17 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 135
health:
  - name: "HP"
    desc: "135; __Immunities__ [[srd/pf2e/compendium/rules-elements/Conditions#Controlled|controlled]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]] 10"
speed: "30 feet, climb 30 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _scimitar_ +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Force|forceful +2]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Sweep|Sweep]]) __Damage__ 2d6+10 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Polymorph|Polymorph]]) The lamia matriarch can take on the appearance of a Medium [[srd/pf2e/compendium/rules-elements/traits/player-core/Humanoid|humanoid]]. This doesn't change their Speed or their attack and damage modifiers with their Strikes, but it does prevent them from using their cursed touch. Each lamia matriarch has a fixed humanoid form that resembles their upper torso when in their true form. This is the only humanoid form they can adopt using this ability."
  - name: "Matriarch's Caress"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]]) The lamia touches a creature, who must succeed at a DC 28 Will save or become [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 2]]. If the target fails additional saves against this ability, the condition value increases by 2 (to a maximum of stupefied 4). This condition value decreases by 1 every 24 hours."
  - name: "Scimitar Storm"
    desc: "⬽ The lamia matriarch makes a scimitar attack against each enemy within reach. Each attack counts toward their multiple attack penalty, but the penalty does not increase until after all the attacks. The first enemy they damage is subject to Matriarch's Caress."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 28 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Bless|Bless]], [[srd/pf2e/compendium/spells/rank-1/Force Barrage|Force Barrage]], [[srd/pf2e/compendium/spells/rank-1/Phantom Pain|Phantom Pain]], [[srd/pf2e/compendium/spells/rank-1/Soothe|Soothe]] (4 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Blur|Blur]], [[srd/pf2e/compendium/spells/rank-2/Illusory Creature|Illusory Creature]], [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]] (4 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-2/Dispel Magic|Dispel Magic]], [[srd/pf2e/compendium/spells/rank-3/Enthrall|Enthrall]], [[srd/pf2e/compendium/spells/rank-3/Haste|Haste]], [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]] (4 slots)"
  - name: "Occult Innate Spells"
    desc: "DC 28 - __1st__ [[srd/pf2e/compendium/spells/rank-1/Ventriloquism|Ventriloquism]] (at will) - __2nd__ [[srd/pf2e/compendium/spells/rank-1/Illusory Disguise|Illusory Disguise]] (at will), [[srd/pf2e/compendium/spells/rank-1/Illusory Object|Illusory Object]] (at will), [[srd/pf2e/compendium/spells/rank-2/Blur|Blur]] - __4th__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]] (×3), [[srd/pf2e/compendium/spells/rank-4/Suggestion|Suggestion]] (×3), [[srd/pf2e/compendium/spells/rank-1/Sleep|Sleep]]"
sourcebook: "_Monster Core_, page 215."
```

```encounter-table
name: Lamia Matriarch
creatures:
  - 1: Lamia Matriarch
```
