namespace Python.OilWell.Api.Models
{
    public class DatabaseSeeded
    {
        public int Id { get; set; }
        public DateTime SeededAt { get; set; }
        public string Description { get; set; } = string.Empty;
    }
}