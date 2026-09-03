---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Caligni Hunter"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/caligni
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Caligni Hunter"
level: 4
source: "Monster Core"
aon_id: "creature-2864"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2864"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Caligni Hunter"
level: "Creature 4"
size: "Medium"
trait_01: "Caligni"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; greater darkvision, light blindness"
languages: "Caligni, [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +13, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +12"
abilityMods: [2, 5, 2, -1, 2, 1]
abilities_top:
  - name: "Items"
    desc: "darkening poison (6 doses), Leather Armor, Shortsword (2)"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +10; __Ref__: +13; __Will__: +8"
hp: 60
health:
  - name: "HP"
    desc: "60 (final fate)"
abilities_mid:
  - name: "Final Fate"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]]) When the hunter dies, their soul leaves their body in an explosion of spiritual energy. All creatures in a 20-foot burst take 5d6 spirit damage (DC 19 basic Will save). The hunter's possessions are left in a pile where they died."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d6+7 piercing plus darkening poison"
abilities_bot:
  - name: "Double Slice"
    desc: "⬺ The caligni hunter makes two Strikes against the same target, one with each of their shortswords. The hunter combines the damage of any attacks that hit and applies precision damage, resistances, and weaknesses only once. Both attacks count toward the hunter's multiple attack penalty, but the penalty increases only after both attacks."
  - name: "Encircling Command"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]]) Each [[srd/pf2e/bestiary/monster-core/humanoid/caligni-skulker|caligni skulker]] within 30 feet of the hunter can Step. Each skulker can benefit from Encircling Command only once per round."
  - name: "Sneak Attack"
    desc: "The caligni hunter deals 1d6 extra precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 19 - __Cantrips (2nd)__ [[srd/pf2e/compendium/spells/cantrips/figment|Figment]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/darkness|Darkness]] (at will), [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]] (at will)"
sourcebook: "_Monster Core_, page 49."
```

```encounter-table
name: Caligni Hunter
creatures:
  - 1: Caligni Hunter
```
