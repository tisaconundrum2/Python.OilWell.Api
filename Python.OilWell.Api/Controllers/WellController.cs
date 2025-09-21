using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Python.OilWell.Api.Models;

namespace Python.OilWell.Api.Controllers;

public class WellController : Controller
{
    private readonly ILogger<WellController> _logger;

    public WellController(ILogger<WellController> logger)
    {
        _logger = logger;
    }

    public IActionResult Index()
    {
        return Redirect("/swagger");
    }

    public IActionResult Privacy()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}