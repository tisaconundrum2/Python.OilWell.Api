namespace Python.OilWell.Api.Models
{
    public class Well
    {
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public string Location { get; set; } = string.Empty;
        public DateTime DrilledAt { get; set; }
        public double Depth { get; set; } // in meters
        public bool IsActive { get; set; }
    }
}