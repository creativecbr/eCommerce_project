<?php

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.

if (\class_exists(\ContainerJqb3bwe\appProdProjectContainer::class, false)) {
    // no-op
} elseif (!include __DIR__.'/ContainerJqb3bwe/appProdProjectContainer.php') {
    touch(__DIR__.'/ContainerJqb3bwe.legacy');

    return;
}

if (!\class_exists(appProdProjectContainer::class, false)) {
    \class_alias(\ContainerJqb3bwe\appProdProjectContainer::class, appProdProjectContainer::class, false);
}

return new \ContainerJqb3bwe\appProdProjectContainer([
    'container.build_hash' => 'Jqb3bwe',
    'container.build_id' => 'c14db996',
    'container.build_time' => 1605219030,
], __DIR__.\DIRECTORY_SEPARATOR.'ContainerJqb3bwe');