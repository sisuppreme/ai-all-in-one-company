# Example 1 — Engine-default scene replaced by a lit, material-true scene

Corrects rule **FE-303** (zero GL tells: GL-01, GL-02, GL-03).

## Before

```js
// The tutorial default: one white ambient light, one gray
// plastic material, camera dead center at the default angle.
// GL-01 + GL-02 + GL-03 in a single file. This is BAN-FE-152.
import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, 1.6, 0.1, 100);
camera.position.set(0, 0, 5); // aimed at the origin, eye level

scene.add(new THREE.AmbientLight(0xffffff, 1)); // no key, no shadow side

const material = new THREE.MeshStandardMaterial({ color: 0x888888 });
const product = new THREE.Mesh(new THREE.BoxGeometry(2, 1, 1), material);
scene.add(product);
```

## After

```js
// A chosen camera, a key light that casts shadows, a fill at
// lower intensity, and materials matched to the real surfaces.
import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(35, 1.6, 0.1, 100);
camera.position.set(3.2, 1.8, 4.2); // three-quarter view, slightly above
camera.lookAt(0, 0.4, 0);

const key = new THREE.DirectionalLight(0xfff2e0, 2.4);
key.position.set(4, 6, 3);
key.castShadow = true;
scene.add(key);
scene.add(new THREE.HemisphereLight(0xdfe8ff, 0x3a3128, 0.5)); // fill, not the only light

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.shadowMap.enabled = true;
renderer.toneMapping = THREE.ACESFilmicToneMapping;

const body = new THREE.Mesh(
  new THREE.BoxGeometry(2, 1, 1),
  new THREE.MeshStandardMaterial({ color: 0x8a2f2b, roughness: 0.55, metalness: 0.05 })
);
body.castShadow = true;
scene.add(body);

const ground = new THREE.Mesh(
  new THREE.PlaneGeometry(20, 20),
  new THREE.ShadowMaterial({ opacity: 0.25 })
);
ground.rotation.x = -Math.PI / 2;
ground.position.y = -0.5;
ground.receiveShadow = true;
scene.add(ground);
```

Note: the before scene is recognizable as engine output before the product is even identified — flat light, one plastic, default camera. The after version gives the product a shadow side, real materials, and a deliberate viewpoint, clearing G-FE-152's GL-01/02/03 checks.
