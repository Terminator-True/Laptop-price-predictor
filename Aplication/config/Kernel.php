<?php 
namespace app\config;

use app\config\Constants;

class Kernel 
{
    private $controller = 'FormController';
    private $method = 'index';


    public function __construct()
    {
        $init = new Constants();
    }
}