<?php


namespace Controllers\Controller;

class Controller
{

    /**
     * Controller base
     * Carga las vistas
     */
    public function view($view_name, $data = [])
    {
        $route =  '../Views/' . $view_name . '.php';
        if (file_exists($route)) {
            require_once $route;
        }

        die('404');
    }
}