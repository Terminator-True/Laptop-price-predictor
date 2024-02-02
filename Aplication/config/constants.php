<?php 
namespace app\config;

use app\config\Configuration;


class Constants
{
    public function __construct()
    {
        $configuration = new Configuration();
        $config = $configuration->get_constants();
        
        
        define('APPROOT', dirname(dirname(__FILE__)));
        define('URLROOT', $config->URLROOT);
        define('SITENAME', $config->SITENAME);        
    }
}


