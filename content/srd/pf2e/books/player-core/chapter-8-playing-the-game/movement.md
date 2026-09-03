---
title: "Movement"
aliases: ["Movement"]
cssclasses:
  - pf2e
  - pf2e-book
tags:
  - srd/pf2e/player-core
source: "Player Core"
aon_id: 2345
aon_url: "https://2e.aonprd.com/Rules.aspx?ID=2345"
citation: "Player Core pg. 420"
---

# Movement

<sup>PC1 p. 420</sup>

Your movement and position determine how you interact with the world. Moving in exploration and downtime modes is relatively fluid. Movement in encounter mode follows additional rules explained in [[#Tactical Movement|Tactical Movement]]. The rules below apply in all modes of play.

## Movement Types

Creatures in Pathfinder soar through the clouds, scale sheer cliffs, and tunnel underfoot. The majority of creatures have a Speed, which is how fast they can move across the ground.

Some abilities give you different ways to move, such as through the air or underground. Each of these special movement types has its own Speed value. Many creatures have these Speeds naturally, such as a bird having a fly Speed or a fish having a swim Speed. The various types of movement are listed below. Since the Stride action can be used only with your normal Speed, moving using one of these movement types requires using a special action, and you can't Step while using one of these movement types. Since Speed by itself refers to your land Speed, rules text concerning these special movement types specifies the movement types to which it applies. Speeds can be increased or decreased with item, circumstance, and status bonuses and penalties. Penalties can't reduce your Speeds below 5 feet unless stated otherwise.

Switching from one movement type to another requires ending your action that has the first movement type and using a new action that has the second movement type. For instance, if you Climbed 10 feet to the top of a cliff, you could then Stride forward 10 feet. In some cases, the GM might rule otherwise, especially if you're moving a very short distance using one of the types of movement.

### Speed

Most characters and monsters have a Speed statistic that indicates how quickly they can move across the ground. This statistic is referred to as land Speed when it's necessary to differentiate it from special Speeds.

When you use the Stride action, you move a number of feet equal to your Speed. Numerous other abilities also allow you to move, from Crawling to Leaping, and most of them are based on your Speed in some way. Whenever a rule mentions your Speed without specifying a type, it's referring to your land Speed.

### Burrow Speed

A burrow Speed lets you tunnel through the ground. You can use the Burrow action if you have a burrow Speed. Burrowing doesn’t normally leave behind a tunnel unless the ability specifically states that it does. Most creatures need to hold their breath when burrowing, and they might need [[srd/pf2e/books/player-core/chapter-8-playing-the-game/perception-and-detection#Tremorsense|tremorsense]] to navigate.

### Climb Speed

A climb Speed allows you to move up or down inclines and vertical surfaces. Most creatures need to succeed at Athletics checks to Climb, but if you have a climb Speed, you automatically succeed and move up to your climb Speed instead of the listed distance.

You might still have to attempt Athletics checks to Climb in hazardous conditions, to Climb extremely difficult surfaces, or to cross horizontal planes such as ceilings. You can also choose to roll an Athletics check to Climb rather than accept an automatic success in hopes of getting a critical success. Your climb Speed grants you a +4 circumstance bonus to Athletics checks to Climb.

If you have a climb Speed, you're not off-guard while you're climbing.

### Fly Speed

As long as you have a fly Speed, you can use the Fly and Arrest a Fall actions. You can also attempt to Maneuver in Flight if you're trained in the Acrobatics skill.

Wind conditions can affect how you use the Fly action. In general, moving against the wind uses the same rules as moving through [[#Difficult Terrain|difficult terrain]] (or greater difficult terrain, if you're also flying upward), and moving with the wind allows you to move 10 feet for every 5 feet of movement you spend (not cumulative with moving straight downward). For more information on spending movement, see [[#Tactical Movement|Tactical Movement]].

Upward and downward movement are both relative to the gravity in your area; if you're in zero gravity, moving up or down is no different from moving horizontally.

### Swim Speed

With a swim Speed, you can propel yourself through the water with little impediment. Instead of attempting Athletics checks to Swim, you automatically succeed and move up to your swim Speed instead of the listed distance. Moving up or down is still moving through [[#Difficult Terrain|difficult terrain]].

You might still have to attempt checks to Swim in hazardous conditions or to cross turbulent water. You can also choose to roll an Athletics check to Swim rather than accept an automatic success in hopes of getting a critical success. Your swim Speed grants you a +4 circumstance bonus to Athletics checks to Swim.

Having a swim Speed doesn't necessarily mean you can breathe in water, so you might still have to hold your breath if you're underwater to avoid [[srd/pf2e/books/player-core/chapter-8-playing-the-game/encounter-mode#Drowning and Suffocating|drowning]].

## Falling

If you fall more than 5 feet, when you land you take bludgeoning damage equal to half the distance you fell. Treat falls longer than 1,500 feet as though they were 1,500 feet (750 damage). If you take any damage from a fall, you land prone. You fall about 500 feet in the first round of falling and about 1,500 feet each round thereafter.

You can Grab an Edge as a reaction to reduce the damage from some falls, or Arrest a Fall if you have a fly Speed. In addition, if you fall into water, snow, or another relatively soft substance, you can treat the fall as though it were 20 feet shorter, or 30 feet shorter if you intentionally dove in. The effective reduction can't be greater than the depth (so when falling into 10-foot-deep water, you treat the fall as 10 feet shorter).

### Falling on a Creature

If you land on a creature, that creature must attempt a DC 15 Reflex save. Intentionally aiming yourself to land on a creature after a long fall is almost impossible.
**Critical Success** The creature takes no damage.
**Success** The creature takes bludgeoning damage equal to one-quarter the falling damage you took.
**Failure** The creature takes bludgeoning damage equal to half the falling damage you took.
**Critical Failure** The creature takes the same amount of bludgeoning damage you took from the fall.

### Falling Objects

A dropped object takes damage just like a falling creature. If the object lands on a creature, that creature can attempt a Reflex save using the same rules as for a creature falling on a creature. Hazards and spells that involve falling objects, such as a rock slide, have their own rules about how they interact with creatures and the damage they deal.

## Tactical Movement

Your movement during encounter mode—and at other times where precise movement matters—depends on the actions and other abilities you use. Whether you Stride, Step, Swim, or Climb, the maximum distance you can move is based on your Speed. Certain feats or magic items can grant you other [[#Movement Types|movement types]], allowing you to swiftly [[#Burrow Speed|burrow]], [[#Climb Speed|climb]], [[#Fly Speed|fly]], or [[#Swim Speed|swim]].

When the rules refer to a “movement cost” or “spending movement,” they are describing how many feet of your Speed you must use to move from one point to another. Normally, movement costs the number of feet you're moving. However, sometimes it's harder to move a certain distance due to [[#Difficult Terrain|difficult terrain]] or other factors. In such a case, you might have to spend a different amount of movement to move from one place to another.

> [!pf2-sidebar] REACTIONS TO MOVEMENT
>
> Some reactions and free actions are triggered by a creature using an action with the move trait. The most notable example is Reactive Strike (reproduced below). Actions with the move trait can trigger reactions or free actions throughout the course of the distance traveled. Each time you exit a square within a creature's reach, your movement triggers those reactions and free actions (although no more than once per move action for a given reacting creature). If you use a move action but don't move out of a square, the trigger instead happens at the end of that action or ability.
>
> Some actions, such as Step, specifically state they don't trigger reactions or free actions based on movement.
>
> ### Reactive Strike [reaction]
>
> **Source** Player Core pg. 138
> **Trigger** A creature within your reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using.
>
> ---
>
> You lash out at a foe that leaves an opening. Make a melee Strike against the triggering creature. If your attack is a critical hit and the trigger was a manipulate action, you disrupt that action. This Strike doesn't count toward your multiple attack penalty, and your multiple attack penalty doesn't apply to this Strike.

### Grid Movement

If an encounter involves combat, it’s often a good idea to track the movement and relative position of the participants using a Pathfinder Flip-Mat or some other form of grid to display the terrain, and miniatures to represent the combatants. When a character moves on a grid, every 1-inch square of the play area is 5 feet across in the game world. Hence, a creature moving in a straight line spends 5 feet of its movement for every map square traveled. [[#Difficult Terrain|Difficult terrain]] can make some squares cost more of your movement.

#### Diagonal Movement

Because moving diagonally covers more ground, you count that movement differently. The first square of diagonal movement you make in a turn counts as 5 feet, but the second counts as 10 feet, and your count thereafter alternates between the two. For example, as you move across 4 squares diagonally, you would count 5 feet, then 10, then 5, and then 10, for a total of 30 feet. You track your total diagonal movement across all your movement during your turn, but reset your count at the end of your turn. The diagram on this page shows an example.

#### 3D Movement

Most movement in a game can be represented on a flat map. If creatures are flying, swimming, or otherwise moving through three-dimensional space, see the advice under [[srd/pf2e/books/player-core/chapter-8-playing-the-game/encounter-mode#Special Battles|Special Battles]].

### Size, Space, and Reach

Creatures and objects of different sizes occupy different amounts of space. The sizes and the spaces they each take up on a grid are listed in the Size and Reach table (see below). The table also lists the typical reach for creatures of each size, for both tall creatures (most bipeds) and long creatures (most quadrupeds). See [[srd/pf2e/books/player-core/chapter-8-playing-the-game/effects#Range and Reach|here]] for more about reach.

The Space entry lists how many feet on a side a creature's space is, so a Large creature fills a 10-foot-by- 10-foot space, or 4 squares on the grid. (If you need to measure in three dimensions, their space is also 10 feet high.) Sometimes part of a creature extends beyond its space, such as if a giant octopus is grabbing you with its tentacles. In that case, the GM will usually allow attacking the extended portion, even if you can't reach the main creature.

## Table 9-1: Size and Reach

| **Size** | **Space** | **Reach (Tall)** | **Reach (Long)** |
| --- | --- | --- | --- |
| Tiny | Less than 5 feet | 0 feet | 0 feet |
| Small | 5 feet | 5 feet | 5 feet |
| Medium | 5 feet | 5 feet | 5 feet |
| Large | 10 feet | 10 feet | 5 feet |
| Huge | 15 feet | 15 feet | 10 feet |
| Gargantuan | 20 feet or more | 20 feet | 15 feet |

A Small or larger creature or object takes up at least 1 square on a grid, and creatures of these sizes can't usually share spaces except in situations like a character riding a mount.

Multiple Tiny creatures can occupy the same square. At least four can fit in a single square, though the GM might determine that even more can fit. Tiny creatures can share a space occupied by a larger creature as well. If a Tiny creature's reach is 0 feet, it must share a space with a creature in order to attack it.

### Moving Through a Creature’s Space

You can move through the space of a willing creature. If you want to move through an unwilling creature’s space, you can Tumble Through it. You can’t end your turn in a square occupied by another creature, though you can end a move action in its square provided that you immediately use another move action to leave that square. If two creatures end up in the same square by accident, the GM determines which one is forced out of the square (or whether one falls prone).

#### Prone and Incapacitated Creatures

You can share a space with a prone creature if that creature is willing, unconscious, or dead and if it is your size or smaller. The GM might allow you to climb atop the corpse or unconscious body of a larger creature in some situations. A prone creature can’t stand up while someone else occupies its space, but it can Crawl to a space where it’s able to stand, or it can attempt to Shove the other creature out of the way.

#### Creatures of Different Sizes

In most cases, you can move through the space of a creature three sizes larger than you or larger. This means a Medium creature can move through the space of a Gargantuan creature and a Small creature can move through the space of a Huge or Gargantuan creature. Likewise, a bigger creature can move through the space of a creature three sizes smaller than itself or smaller. You still can't end your movement in a space occupied by a creature.

Tiny creatures are an exception, just like with sharing a space. They can move through creatures' spaces and can even end their movement there.

Similarly, other creatures can move through and end their movement in a Tiny creature's space.

#### Objects

Because objects aren’t as mobile as creatures are, they’re more likely to fill a space. This means you can’t always move through their spaces like you might move through a space occupied by a creature. You might be able to occupy the same square as a statue of your size, but not a wide column. The GM determines whether you can move into an object’s square normally, whether special rules apply, or if you are unable to move into the square at all.

### Forced Movement

When an effect forces you to move, or if you start [[#Falling|falling]], the distance you move is defined by the effect that moved you, not by your Speed. Forced movement doesn't trigger reactions that are triggered by movement. Some common causes of forced movement include the Reposition and Shove actions of Athletics. In the rare cases where it's unclear whether your movement is voluntary or forced, the GM makes the determination.

If forced movement would move you into a space you can't occupy—because objects are in the way or because you lack the movement type needed to reach it, for example—you stop moving in the last space you can occupy.

Usually the creature or effect forcing the movement chooses the path the victim takes. If you're pushed or pulled, you can usually be moved through [[#Hazardous Terrain|hazardous terrain]], pushed off a ledge, or the like. Abilities that reposition you in some other way can't put you in such dangerous places unless they specify otherwise. In all cases, the GM makes the final call if there's doubt on where forced movement can move a creature.

Some abilities allow a creature to move while carrying another along with it. This is forced movement for the carried creature. Unless noted otherwise, they both move on the same path while this happens—the carrying creature can't drag its victim through dangers while avoiding them itself, for example.

## Terrain

Several types of terrain can complicate your movement by slowing you down, damaging you, or endangering you. Navigating these types of terrain can be challenging, but it can also let you get an advantage over your foes.

### Difficult Terrain

Difficult terrain is any terrain that impedes your movement, ranging from particularly rough or unstable surfaces to thick ground cover and countless other impediments. Moving into a square of **difficult terrain** (or moving 5 feet into or within an area of difficult terrain, if you're not using a grid) costs an extra 5 feet of movement. Moving into a square of **greater difficult terrain** instead costs 10 additional feet of movement. This additional cost is not increased further when moving diagonally. You can't Step into difficult terrain.

Movement you make while jumping ignores the terrain you're jumping over. Some abilities (such as flight or being incorporeal) allow you to avoid the movement reduction from some types of difficult terrain.

#### Ignore Difficult Terrain

Certain abilities let you ignore difficult terrain. If you can ignore difficult terrain, you can also move through greater difficult terrain at the extra movement cost difficult terrain normally imposes. An ability doesn’t let you entirely ignore greater difficult terrain unless the ability specifies otherwise.

### Hazardous Terrain

Hazardous terrain damages you whenever you move through it. An acid pool and a pit of burning embers are both examples of hazardous terrain. The amount and type of damage depend on the specific hazardous terrain.

### Narrow Surfaces

A narrow surface is so precariously thin that you need to Balance or risk falling. Even on a success, you are off-guard on a narrow surface. Each time you are hit by an attack or fail a save on a narrow surface, you must succeed at a Reflex save (with the same DC as the Acrobatics check to Balance) or [[#Falling|fall]].

### Uneven Ground

Uneven ground is an area unsteady enough that you need to Balance or risk falling prone and possibly injuring yourself, depending on the specifics of the uneven ground. You are off-guard on uneven ground. Each time you are hit by an attack or fail a save on uneven ground, you must succeed at a Reflex save (with the same DC as the Acrobatics check to Balance) or fall prone.

### Inclines

An incline is an area so steep that you need to Climb using the Athletics skill in order to progress upward. You’re off-guard when Climbing an incline.

## Cover

When you're behind an obstacle that could block weapons, guard you against explosions, and make you harder to detect, you're behind cover. Standard cover gives you a +2 circumstance bonus to AC, to Reflex saves against area effects, and to Stealth checks to Hide, Sneak, or otherwise avoid detection. You can increase this to greater cover using the Take Cover basic action, increasing the circumstance bonus to +4. If cover is especially light, typically when it's provided by a creature, you have lesser cover, which grants a +1 circumstance bonus to AC. A creature with standard cover or greater cover can attempt to use Stealth to Hide, but lesser cover isn't sufficient.

## Cover

| **Type of Cover** | **Bonus** | **Can Hide** |
| --- | --- | --- |
| Lesser | +1 to AC | No |
| Standard | +2 to AC, Reflex, Stealth | Yes |
| Greater | +4 to AC, Reflex, Stealth | Yes |

Cover is relative, so you might simultaneously have cover against one creature and not another. Cover applies only if your path to the target is partially blocked. If a creature is entirely behind a wall or the like, you don't have [[srd/pf2e/books/player-core/chapter-8-playing-the-game/effects#Line of Effect|line of effect]] and typically can't target it at all.

Usually, the GM can quickly decide whether your target has cover. If you're uncertain or need to be more precise, draw a line from the center of your space to the center of the target's space. If that line passes through any terrain or object that would block the effect, the target has standard cover (or greater cover if the obstruction is extreme or the target has Taken Cover). If the line passes through a creature instead, the target has lesser cover. When measuring cover against an area effect, draw the line from the effect's point of origin to the center of the creature's space. See the diagram for examples.

### Cover and Large Creatures

If a creature between you and a target is two or more sizes larger than both you and your target, that creature’s space blocks the effect enough to provide standard cover instead of lesser cover. The GM might determine that a creature doesn’t gain cover from terrain that it’s significantly larger than. For example, a Huge dragon probably wouldn’t receive any benefit from being behind a 1-foot-wide pillar.

### Special Circumstances

Your GM might allow you to overcome your target’s cover in some situations. If you’re right next to an arrow slit, you can shoot without penalty, but you have greater cover against someone shooting back at you from far away. Your GM might let you reduce or negate cover by leaning around a corner to shoot or the like. This usually takes an action to set up, and the GM might measure cover from an edge or corner of your space instead of your center.

## Flanking

When you and an ally are flanking a foe, it has a harder time defending against you. A creature is off-guard (taking a –2 circumstance penalty to AC) to melee attacks from creatures that are flanking it.

To flank a foe, you and your ally must be on opposite sides of the creature. A line drawn between the center of your space and the center of your ally's space must pass through opposite sides or opposite corners of the foe's space. Additionally, both you and the ally have to be able to act, you must be wielding melee weapons or be able to make an unarmed attack, you can't be under any effects that prevent you from attacking, and you must both have the enemy within reach. If you are wielding a reach weapon, you use your reach with that weapon for this purpose.

> [!pf2-sidebar] TINY CREATURES AND FLANKING
>
> Tiny creatures usually have reach of 0 feet and need to be in a creature's space to attack it. This makes a Tiny creature unable to flank unless it's able to use a weapon with reach or has a melee unarmed attack with reach greater than 0 feet.
>
> The GM might allow Tiny creatures to flank other Tiny creatures if they're all in the same square, but this is best left for special circumstances and uses the GM's best judgment.

> [!pf2-sidebar] AVOIDING FLANKING
>
> Flanking is an excellent battle tactic that can cause the flanked creature to get hit much more often. Escaping and avoiding flanks can be crucial for a player character's survival.
>
> **Movement:** The most straightforward means to escape a flank is usually to Stride. It's often worth it to avoid the hits you'd take due to being off-guard and to make enemies spend actions moving to catch you.
>
> **All-Around Vision:** Some monsters are covered in eyes that face multiple directions or are otherwise hard to distract, making them immune to flanking.
>
> **Deny Advantage:** Some classes, such as rogue, can gain the deny advantage class feature, makes them harder to outflank. You can't flank a creature with deny advantage unless your level is higher than the creature's.

### 3D Flanking

Though battle grids are often two-dimensional, the game world isn't! Sometimes you might need to visualize a creature's space as a cube for flanking. For instance, if Valeros is underneath a flying sphinx while Lini is flying above the sphinx, they might be flanking it even if they're piled in an odd stack on your battle grid. And if Valeros were mounted on a horse, he might be able to measure from farther off the ground than normal.

In these cases, it's usually best to have the GM make the call on who's flanking rather than trying to do meticulous measurements in three dimensions.
