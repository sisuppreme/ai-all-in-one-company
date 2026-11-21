# Example 1 — Blank list replaced by a designed empty state

## Before

```html
<section class="projects">
  <!-- projects.length === 0 renders nothing at all -->
</section>
```

A new account's Projects page is a heading above a white void. The user cannot
tell whether the page is broken, still loading, or genuinely empty — and has
no next step.

## After

```html
<section class="projects">
  <div class="empty-state">
    <h2>No projects yet</h2>
    <p>Projects keep your boards, files, and deadlines in one place.
       Create your first project to get started.</p>
    <button class="btn-primary" data-action="create-project">
      Create a project
    </button>
    <p class="empty-state-alt">
      Or <a href="/templates">start from a template</a>.
    </p>
  </div>
</section>
```

The empty state names the condition, explains what belongs here, and offers
the primary next action plus an alternative. The no-results variant of the
same view differs on purpose: "No projects match 'harbor'" with a
"Clear search" action — a different state, not the same copy reused.

Note: corrects FE-167 — empty states explain what belongs here and offer the next action; first-use and no-results are different states.
