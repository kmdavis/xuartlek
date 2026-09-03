---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Desert Drake"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/large
statblock: inline
name: "Desert Drake"
level: 8
source: "Monster Core"
aon_id: "creature-2963"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2963"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Desert Drake"
level: "Creature 8"
size: "Large"
trait_01: "Dragon"
trait_02: "Earth"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, sandstorm sight, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +13, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +15"
abilityMods: [6, 3, 5, -1, 3, 1]
abilities_top:
  - name: "Sandstorm Sight"
    desc: "Sandstorms don't impair a desert drake's vision; they ignore [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealment]]from sandstorms. They also are immune to being [[srd/pf2e/compendium/rules-elements/conditions#Dazzled|dazzled]] or [[srd/pf2e/compendium/rules-elements/conditions#Blinded|blinded]] by sand or other grit."
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +17; __Ref__: +15; __Will__: +13"
hp: 135
health:
  - name: "HP"
    desc: "135; __Immunities__ [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 10 **Wing Deflection ⬲"
abilities_mid:
  - name: "Trigger"
    desc: "The desert drake is targeted with an attack**"
  - name: "Effect"
    desc: "The desert drake raises their wing, gaining a +2 circumstance bonus to AC against the triggering attack. If the desert drake is flying at the time they're attacked, they descend 10 feet after the attack is complete."
speed: "20 feet; burrow 20 feet (sand only), fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +19 __Damage__ 2d12+10 piercing"
  - name: "Melee"
    desc: "⬻ tail +19 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d8+10 bludgeoning plus Push 5 feet"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The desert drake makes two fangs Strikes and one tail Strike in any order."
  - name: "Sandstorm Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The desert drake spits a ball of abrasive sand with a range of 60 feet that explodes into a cloud with a 15-foot-radius burst. Creatures in the area take 9d6 slashing damage (DC 27 basic Reflex save). The desert drake can't use Sandstorm Breath again for 1d6 rounds, during which the sandstorm lingers in the area. This lingering sandstorm grants [[srd/pf2e/compendium/rules-elements/conditions#Concealed|concealment]]to everything within it and conceals everything outside from them."
  - name: "Speed Surge"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|Move]])"
  - name: "Frequency"
    desc: "three times per day"
  - name: "Effect"
    desc: "The desert drake Strides or Flies twice."
  - name: "Surprise Attacker"
    desc: "On the first round of combat, creatures that haven't acted yet are [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] to the desert drake."
sourcebook: "_Monster Core_, page 133."
```

```encounter-table
name: Desert Drake
creatures:
  - 1: Desert Drake
```
