using Microsoft.EntityFrameworkCore;
using Python.OilWell.Api.Models;

namespace Python.OilWell.Api.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }

        public DbSet<DatabaseSeeded> DatabaseSeeded { get; set; }
        public DbSet<Well> Wells { get; set; }
    }
}