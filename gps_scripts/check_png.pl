package check_png;
use warnings FATAL => 'all';

use GD;

print GD::Image->can('png') ? "PNG supported\n" : "PNG not supported\n";
